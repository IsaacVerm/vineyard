const credentials = require('./credentials');

const puppeteer = require('puppeteer');

(async () => {
  /// selectors
  const usernameInput = 'table #ctl00_ContentPlaceHolder1_Login1_UserName';
  const passwordInput = 'table #ctl00_ContentPlaceHolder1_Login1_Password';
  const loginButton = 'table #ctl00_ContentPlaceHolder1_Login1_LoginButton';
  const weatherStation =
    '#ctl00_ContentPlaceHolder1_gvStuurmodules > tbody > tr:nth-child(3) > td:nth-child(3)';
  const dataOverview = '#__tab_ctl00_ContentPlaceHolder1_TabContainer1_tpData';
  const startDateExport = 'table #ctl00_ContentPlaceHolder1_TabContainer1_tpData_txtBeginExport';
  const endDateExport = 'table #ctl00_ContentPlaceHolder1_TabContainer1_tpData_txtEindExport';
  const exportButton = 'table #ctl00_ContentPlaceHolder1_TabContainer1_tpData_btnExportData';

  // get browser and page
  const browser = await puppeteer.launch({ headless: false });
  const page = await browser.newPage();

  // go to login page
  await page.goto('http://sensornetwerk.inagro.be');

  // fill in credentials
  await page.type(usernameInput, credentials.username);
  await page.type(passwordInput, credentials.password);
  await page.click(loginButton);

  // select weather station
  await page.waitForSelector(weatherStation);
  await page.click(weatherStation);

  // go to data overview
  await page.waitForSelector(dataOverview);
  await page.click(dataOverview);

  // fill in start and end date export
  await page.waitForSelector(startDateExport);
  await page.$eval(startDateExport, el => (el.value = '01/01/2019'));
  await page.waitForSelector(endDateExport);
  await page.$eval(endDateExport, el => (el.value = '31/12/2019'));

  // export
  await page.waitForSelector(exportButton);
  await page.click(exportButton);

  // close browser
  await page.waitFor(120000); // wait 2 minutes till download is finished to close browser
  await browser.close();
})();
