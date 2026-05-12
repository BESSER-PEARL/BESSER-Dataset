





import java.util.List;
import java.util.ArrayList;

public class SpreadsheetMLStyles_ExcelWorkbook  {

    private String refModeR1C1;
    private String acceptLabelsInFormulas;
    private String protectStructure;
    private String doNotCalculateBeforeSave;
    private String maxChange;
    private String createBackup;
    private String activeSheet;
    private String tabRatio;
    private String noAutoRecover;
    private String windowTopX;
    private String windowIconic;
    private String firstVisibleSheet;
    private String doNotSaveLinkValues;
    private String precisionAsDisplayed;
    private String futureVer;
    private String hideWorkbookTabs;
    private String windowHidden;
    private String embedSaveSmartTags;
    private String calculation;
    private String windowTopY;
    private String displayDrawingObjects;
    private String windowHeight;
    private String iteration;
    private String windowWidth;
    private String activeChart;
    private String hideVerticalScrollBar;
    private String protectWindows;
    private String uncalced;
    private String displayInkNotes;
    private String selectedSheets;
    private String hidePivotTableFieldList;
    private String date1904;
    private String hideHorizontalScrollBar;
    private String maxIterations;





    private Workbook workbook;


    public SpreadsheetMLStyles_ExcelWorkbook(
        String refModeR1C1,        String acceptLabelsInFormulas,        String protectStructure,        String doNotCalculateBeforeSave,        String maxChange,        String createBackup,        String activeSheet,        String tabRatio,        String noAutoRecover,        String windowTopX,        String windowIconic,        String firstVisibleSheet,        String doNotSaveLinkValues,        String precisionAsDisplayed,        String futureVer,        String hideWorkbookTabs,        String windowHidden,        String embedSaveSmartTags,        String calculation,        String windowTopY,        String displayDrawingObjects,        String windowHeight,        String iteration,        String windowWidth,        String activeChart,        String hideVerticalScrollBar,        String protectWindows,        String uncalced,        String displayInkNotes,        String selectedSheets,        String hidePivotTableFieldList,        String date1904,        String hideHorizontalScrollBar,        String maxIterations    ) {
        this.refModeR1C1 = refModeR1C1;
        this.acceptLabelsInFormulas = acceptLabelsInFormulas;
        this.protectStructure = protectStructure;
        this.doNotCalculateBeforeSave = doNotCalculateBeforeSave;
        this.maxChange = maxChange;
        this.createBackup = createBackup;
        this.activeSheet = activeSheet;
        this.tabRatio = tabRatio;
        this.noAutoRecover = noAutoRecover;
        this.windowTopX = windowTopX;
        this.windowIconic = windowIconic;
        this.firstVisibleSheet = firstVisibleSheet;
        this.doNotSaveLinkValues = doNotSaveLinkValues;
        this.precisionAsDisplayed = precisionAsDisplayed;
        this.futureVer = futureVer;
        this.hideWorkbookTabs = hideWorkbookTabs;
        this.windowHidden = windowHidden;
        this.embedSaveSmartTags = embedSaveSmartTags;
        this.calculation = calculation;
        this.windowTopY = windowTopY;
        this.displayDrawingObjects = displayDrawingObjects;
        this.windowHeight = windowHeight;
        this.iteration = iteration;
        this.windowWidth = windowWidth;
        this.activeChart = activeChart;
        this.hideVerticalScrollBar = hideVerticalScrollBar;
        this.protectWindows = protectWindows;
        this.uncalced = uncalced;
        this.displayInkNotes = displayInkNotes;
        this.selectedSheets = selectedSheets;
        this.hidePivotTableFieldList = hidePivotTableFieldList;
        this.date1904 = date1904;
        this.hideHorizontalScrollBar = hideHorizontalScrollBar;
        this.maxIterations = maxIterations;
    }


    public String getRefmoder1c1() {
        return refModeR1C1;
    }

    public void setRefmoder1c1(String refModeR1C1) {
        this.refModeR1C1 = refModeR1C1;
    }
    public String getAcceptlabelsinformulas() {
        return acceptLabelsInFormulas;
    }

    public void setAcceptlabelsinformulas(String acceptLabelsInFormulas) {
        this.acceptLabelsInFormulas = acceptLabelsInFormulas;
    }
    public String getProtectstructure() {
        return protectStructure;
    }

    public void setProtectstructure(String protectStructure) {
        this.protectStructure = protectStructure;
    }
    public String getDonotcalculatebeforesave() {
        return doNotCalculateBeforeSave;
    }

    public void setDonotcalculatebeforesave(String doNotCalculateBeforeSave) {
        this.doNotCalculateBeforeSave = doNotCalculateBeforeSave;
    }
    public String getMaxchange() {
        return maxChange;
    }

    public void setMaxchange(String maxChange) {
        this.maxChange = maxChange;
    }
    public String getCreatebackup() {
        return createBackup;
    }

    public void setCreatebackup(String createBackup) {
        this.createBackup = createBackup;
    }
    public String getActivesheet() {
        return activeSheet;
    }

    public void setActivesheet(String activeSheet) {
        this.activeSheet = activeSheet;
    }
    public String getTabratio() {
        return tabRatio;
    }

    public void setTabratio(String tabRatio) {
        this.tabRatio = tabRatio;
    }
    public String getNoautorecover() {
        return noAutoRecover;
    }

    public void setNoautorecover(String noAutoRecover) {
        this.noAutoRecover = noAutoRecover;
    }
    public String getWindowtopx() {
        return windowTopX;
    }

    public void setWindowtopx(String windowTopX) {
        this.windowTopX = windowTopX;
    }
    public String getWindowiconic() {
        return windowIconic;
    }

    public void setWindowiconic(String windowIconic) {
        this.windowIconic = windowIconic;
    }
    public String getFirstvisiblesheet() {
        return firstVisibleSheet;
    }

    public void setFirstvisiblesheet(String firstVisibleSheet) {
        this.firstVisibleSheet = firstVisibleSheet;
    }
    public String getDonotsavelinkvalues() {
        return doNotSaveLinkValues;
    }

    public void setDonotsavelinkvalues(String doNotSaveLinkValues) {
        this.doNotSaveLinkValues = doNotSaveLinkValues;
    }
    public String getPrecisionasdisplayed() {
        return precisionAsDisplayed;
    }

    public void setPrecisionasdisplayed(String precisionAsDisplayed) {
        this.precisionAsDisplayed = precisionAsDisplayed;
    }
    public String getFuturever() {
        return futureVer;
    }

    public void setFuturever(String futureVer) {
        this.futureVer = futureVer;
    }
    public String getHideworkbooktabs() {
        return hideWorkbookTabs;
    }

    public void setHideworkbooktabs(String hideWorkbookTabs) {
        this.hideWorkbookTabs = hideWorkbookTabs;
    }
    public String getWindowhidden() {
        return windowHidden;
    }

    public void setWindowhidden(String windowHidden) {
        this.windowHidden = windowHidden;
    }
    public String getEmbedsavesmarttags() {
        return embedSaveSmartTags;
    }

    public void setEmbedsavesmarttags(String embedSaveSmartTags) {
        this.embedSaveSmartTags = embedSaveSmartTags;
    }
    public String getCalculation() {
        return calculation;
    }

    public void setCalculation(String calculation) {
        this.calculation = calculation;
    }
    public String getWindowtopy() {
        return windowTopY;
    }

    public void setWindowtopy(String windowTopY) {
        this.windowTopY = windowTopY;
    }
    public String getDisplaydrawingobjects() {
        return displayDrawingObjects;
    }

    public void setDisplaydrawingobjects(String displayDrawingObjects) {
        this.displayDrawingObjects = displayDrawingObjects;
    }
    public String getWindowheight() {
        return windowHeight;
    }

    public void setWindowheight(String windowHeight) {
        this.windowHeight = windowHeight;
    }
    public String getIteration() {
        return iteration;
    }

    public void setIteration(String iteration) {
        this.iteration = iteration;
    }
    public String getWindowwidth() {
        return windowWidth;
    }

    public void setWindowwidth(String windowWidth) {
        this.windowWidth = windowWidth;
    }
    public String getActivechart() {
        return activeChart;
    }

    public void setActivechart(String activeChart) {
        this.activeChart = activeChart;
    }
    public String getHideverticalscrollbar() {
        return hideVerticalScrollBar;
    }

    public void setHideverticalscrollbar(String hideVerticalScrollBar) {
        this.hideVerticalScrollBar = hideVerticalScrollBar;
    }
    public String getProtectwindows() {
        return protectWindows;
    }

    public void setProtectwindows(String protectWindows) {
        this.protectWindows = protectWindows;
    }
    public String getUncalced() {
        return uncalced;
    }

    public void setUncalced(String uncalced) {
        this.uncalced = uncalced;
    }
    public String getDisplayinknotes() {
        return displayInkNotes;
    }

    public void setDisplayinknotes(String displayInkNotes) {
        this.displayInkNotes = displayInkNotes;
    }
    public String getSelectedsheets() {
        return selectedSheets;
    }

    public void setSelectedsheets(String selectedSheets) {
        this.selectedSheets = selectedSheets;
    }
    public String getHidepivottablefieldlist() {
        return hidePivotTableFieldList;
    }

    public void setHidepivottablefieldlist(String hidePivotTableFieldList) {
        this.hidePivotTableFieldList = hidePivotTableFieldList;
    }
    public String getDate1904() {
        return date1904;
    }

    public void setDate1904(String date1904) {
        this.date1904 = date1904;
    }
    public String getHidehorizontalscrollbar() {
        return hideHorizontalScrollBar;
    }

    public void setHidehorizontalscrollbar(String hideHorizontalScrollBar) {
        this.hideHorizontalScrollBar = hideHorizontalScrollBar;
    }
    public String getMaxiterations() {
        return maxIterations;
    }

    public void setMaxiterations(String maxIterations) {
        this.maxIterations = maxIterations;
    }

    public Workbook getWorkbook() {
        return workbook;
    }

    public void setWorkbook(Workbook workbook) {
        this.workbook = workbook;
    }

}