





import java.util.List;
import java.util.ArrayList;

public class SpreadsheetMLPrintingSetup_WorksheetOptionsElt  {

    private String displayPageBreak;
    private String excelWorksheetType;
    private String allowSizeCols;
    private String frozenNoSplit;
    private String gridlineColor;
    private String doNotDisplayRowHeaders;
    private String leftColumnVisible;
    private String splitVertical;
    private String filterOn;
    private String defaultRowHeight;
    private String allowUsePivotTables;
    private String codeName;
    private String activeRow;
    private String gridlineColorIndex;
    private String fitToPage;
    private String allowInsertRows;
    private String doNotDisplayOutline;
    private String transitionExpressionEvaluation;
    private String allowDeleteRows;
    private String allowSort;
    private String pageBreakZoom;
    private String applyAutomaticOutlineStyles;
    private String noSummaryRowsBelowDetail;
    private String defaultColumnWidth;
    private String zoom;
    private String allowDeleteCols;
    private String rangeSelection;
    private String protectScenarios;
    private String selected;
    private String displayFormulas;
    private String transitionFormulaEntry;
    private String doNotDisplayGridlines;
    private String allowSizeRows;
    private String activeColumn;
    private String tabColorIndex;
    private String showPageBreakZoom;
    private String leftColumnRightPane;
    private String doNotDisplayHeadings;
    private String intlMacro;
    private String noSummaryColumnsRightDetail;
    private String activePane;
    private String displayRightToLeft;
    private String splitHorizontal;
    private String enableSelection;
    private String protectContentst;
    private String doNotDisplayColHeaders;
    private String protectObjects;
    private String doNotDisplayZeros;
    private String allowInsertHyperlinks;
    private String allowFilter;
    private String freezePanes;
    private String topRowBottomPane;
    private String unsynced;
    private String topRowVisible;
    private String standardWidth;
    private String allowInsertCols;
    private String name;
    private String allowFormatCells;
    private String visible;





    private Worksheet worksheet;


    public SpreadsheetMLPrintingSetup_WorksheetOptionsElt(
        String displayPageBreak,        String excelWorksheetType,        String allowSizeCols,        String frozenNoSplit,        String gridlineColor,        String doNotDisplayRowHeaders,        String leftColumnVisible,        String splitVertical,        String filterOn,        String defaultRowHeight,        String allowUsePivotTables,        String codeName,        String activeRow,        String gridlineColorIndex,        String fitToPage,        String allowInsertRows,        String doNotDisplayOutline,        String transitionExpressionEvaluation,        String allowDeleteRows,        String allowSort,        String pageBreakZoom,        String applyAutomaticOutlineStyles,        String noSummaryRowsBelowDetail,        String defaultColumnWidth,        String zoom,        String allowDeleteCols,        String rangeSelection,        String protectScenarios,        String selected,        String displayFormulas,        String transitionFormulaEntry,        String doNotDisplayGridlines,        String allowSizeRows,        String activeColumn,        String tabColorIndex,        String showPageBreakZoom,        String leftColumnRightPane,        String doNotDisplayHeadings,        String intlMacro,        String noSummaryColumnsRightDetail,        String activePane,        String displayRightToLeft,        String splitHorizontal,        String enableSelection,        String protectContentst,        String doNotDisplayColHeaders,        String protectObjects,        String doNotDisplayZeros,        String allowInsertHyperlinks,        String allowFilter,        String freezePanes,        String topRowBottomPane,        String unsynced,        String topRowVisible,        String standardWidth,        String allowInsertCols,        String name,        String allowFormatCells,        String visible    ) {
        this.displayPageBreak = displayPageBreak;
        this.excelWorksheetType = excelWorksheetType;
        this.allowSizeCols = allowSizeCols;
        this.frozenNoSplit = frozenNoSplit;
        this.gridlineColor = gridlineColor;
        this.doNotDisplayRowHeaders = doNotDisplayRowHeaders;
        this.leftColumnVisible = leftColumnVisible;
        this.splitVertical = splitVertical;
        this.filterOn = filterOn;
        this.defaultRowHeight = defaultRowHeight;
        this.allowUsePivotTables = allowUsePivotTables;
        this.codeName = codeName;
        this.activeRow = activeRow;
        this.gridlineColorIndex = gridlineColorIndex;
        this.fitToPage = fitToPage;
        this.allowInsertRows = allowInsertRows;
        this.doNotDisplayOutline = doNotDisplayOutline;
        this.transitionExpressionEvaluation = transitionExpressionEvaluation;
        this.allowDeleteRows = allowDeleteRows;
        this.allowSort = allowSort;
        this.pageBreakZoom = pageBreakZoom;
        this.applyAutomaticOutlineStyles = applyAutomaticOutlineStyles;
        this.noSummaryRowsBelowDetail = noSummaryRowsBelowDetail;
        this.defaultColumnWidth = defaultColumnWidth;
        this.zoom = zoom;
        this.allowDeleteCols = allowDeleteCols;
        this.rangeSelection = rangeSelection;
        this.protectScenarios = protectScenarios;
        this.selected = selected;
        this.displayFormulas = displayFormulas;
        this.transitionFormulaEntry = transitionFormulaEntry;
        this.doNotDisplayGridlines = doNotDisplayGridlines;
        this.allowSizeRows = allowSizeRows;
        this.activeColumn = activeColumn;
        this.tabColorIndex = tabColorIndex;
        this.showPageBreakZoom = showPageBreakZoom;
        this.leftColumnRightPane = leftColumnRightPane;
        this.doNotDisplayHeadings = doNotDisplayHeadings;
        this.intlMacro = intlMacro;
        this.noSummaryColumnsRightDetail = noSummaryColumnsRightDetail;
        this.activePane = activePane;
        this.displayRightToLeft = displayRightToLeft;
        this.splitHorizontal = splitHorizontal;
        this.enableSelection = enableSelection;
        this.protectContentst = protectContentst;
        this.doNotDisplayColHeaders = doNotDisplayColHeaders;
        this.protectObjects = protectObjects;
        this.doNotDisplayZeros = doNotDisplayZeros;
        this.allowInsertHyperlinks = allowInsertHyperlinks;
        this.allowFilter = allowFilter;
        this.freezePanes = freezePanes;
        this.topRowBottomPane = topRowBottomPane;
        this.unsynced = unsynced;
        this.topRowVisible = topRowVisible;
        this.standardWidth = standardWidth;
        this.allowInsertCols = allowInsertCols;
        this.name = name;
        this.allowFormatCells = allowFormatCells;
        this.visible = visible;
    }


    public String getDisplaypagebreak() {
        return displayPageBreak;
    }

    public void setDisplaypagebreak(String displayPageBreak) {
        this.displayPageBreak = displayPageBreak;
    }
    public String getExcelworksheettype() {
        return excelWorksheetType;
    }

    public void setExcelworksheettype(String excelWorksheetType) {
        this.excelWorksheetType = excelWorksheetType;
    }
    public String getAllowsizecols() {
        return allowSizeCols;
    }

    public void setAllowsizecols(String allowSizeCols) {
        this.allowSizeCols = allowSizeCols;
    }
    public String getFrozennosplit() {
        return frozenNoSplit;
    }

    public void setFrozennosplit(String frozenNoSplit) {
        this.frozenNoSplit = frozenNoSplit;
    }
    public String getGridlinecolor() {
        return gridlineColor;
    }

    public void setGridlinecolor(String gridlineColor) {
        this.gridlineColor = gridlineColor;
    }
    public String getDonotdisplayrowheaders() {
        return doNotDisplayRowHeaders;
    }

    public void setDonotdisplayrowheaders(String doNotDisplayRowHeaders) {
        this.doNotDisplayRowHeaders = doNotDisplayRowHeaders;
    }
    public String getLeftcolumnvisible() {
        return leftColumnVisible;
    }

    public void setLeftcolumnvisible(String leftColumnVisible) {
        this.leftColumnVisible = leftColumnVisible;
    }
    public String getSplitvertical() {
        return splitVertical;
    }

    public void setSplitvertical(String splitVertical) {
        this.splitVertical = splitVertical;
    }
    public String getFilteron() {
        return filterOn;
    }

    public void setFilteron(String filterOn) {
        this.filterOn = filterOn;
    }
    public String getDefaultrowheight() {
        return defaultRowHeight;
    }

    public void setDefaultrowheight(String defaultRowHeight) {
        this.defaultRowHeight = defaultRowHeight;
    }
    public String getAllowusepivottables() {
        return allowUsePivotTables;
    }

    public void setAllowusepivottables(String allowUsePivotTables) {
        this.allowUsePivotTables = allowUsePivotTables;
    }
    public String getCodename() {
        return codeName;
    }

    public void setCodename(String codeName) {
        this.codeName = codeName;
    }
    public String getActiverow() {
        return activeRow;
    }

    public void setActiverow(String activeRow) {
        this.activeRow = activeRow;
    }
    public String getGridlinecolorindex() {
        return gridlineColorIndex;
    }

    public void setGridlinecolorindex(String gridlineColorIndex) {
        this.gridlineColorIndex = gridlineColorIndex;
    }
    public String getFittopage() {
        return fitToPage;
    }

    public void setFittopage(String fitToPage) {
        this.fitToPage = fitToPage;
    }
    public String getAllowinsertrows() {
        return allowInsertRows;
    }

    public void setAllowinsertrows(String allowInsertRows) {
        this.allowInsertRows = allowInsertRows;
    }
    public String getDonotdisplayoutline() {
        return doNotDisplayOutline;
    }

    public void setDonotdisplayoutline(String doNotDisplayOutline) {
        this.doNotDisplayOutline = doNotDisplayOutline;
    }
    public String getTransitionexpressionevaluation() {
        return transitionExpressionEvaluation;
    }

    public void setTransitionexpressionevaluation(String transitionExpressionEvaluation) {
        this.transitionExpressionEvaluation = transitionExpressionEvaluation;
    }
    public String getAllowdeleterows() {
        return allowDeleteRows;
    }

    public void setAllowdeleterows(String allowDeleteRows) {
        this.allowDeleteRows = allowDeleteRows;
    }
    public String getAllowsort() {
        return allowSort;
    }

    public void setAllowsort(String allowSort) {
        this.allowSort = allowSort;
    }
    public String getPagebreakzoom() {
        return pageBreakZoom;
    }

    public void setPagebreakzoom(String pageBreakZoom) {
        this.pageBreakZoom = pageBreakZoom;
    }
    public String getApplyautomaticoutlinestyles() {
        return applyAutomaticOutlineStyles;
    }

    public void setApplyautomaticoutlinestyles(String applyAutomaticOutlineStyles) {
        this.applyAutomaticOutlineStyles = applyAutomaticOutlineStyles;
    }
    public String getNosummaryrowsbelowdetail() {
        return noSummaryRowsBelowDetail;
    }

    public void setNosummaryrowsbelowdetail(String noSummaryRowsBelowDetail) {
        this.noSummaryRowsBelowDetail = noSummaryRowsBelowDetail;
    }
    public String getDefaultcolumnwidth() {
        return defaultColumnWidth;
    }

    public void setDefaultcolumnwidth(String defaultColumnWidth) {
        this.defaultColumnWidth = defaultColumnWidth;
    }
    public String getZoom() {
        return zoom;
    }

    public void setZoom(String zoom) {
        this.zoom = zoom;
    }
    public String getAllowdeletecols() {
        return allowDeleteCols;
    }

    public void setAllowdeletecols(String allowDeleteCols) {
        this.allowDeleteCols = allowDeleteCols;
    }
    public String getRangeselection() {
        return rangeSelection;
    }

    public void setRangeselection(String rangeSelection) {
        this.rangeSelection = rangeSelection;
    }
    public String getProtectscenarios() {
        return protectScenarios;
    }

    public void setProtectscenarios(String protectScenarios) {
        this.protectScenarios = protectScenarios;
    }
    public String getSelected() {
        return selected;
    }

    public void setSelected(String selected) {
        this.selected = selected;
    }
    public String getDisplayformulas() {
        return displayFormulas;
    }

    public void setDisplayformulas(String displayFormulas) {
        this.displayFormulas = displayFormulas;
    }
    public String getTransitionformulaentry() {
        return transitionFormulaEntry;
    }

    public void setTransitionformulaentry(String transitionFormulaEntry) {
        this.transitionFormulaEntry = transitionFormulaEntry;
    }
    public String getDonotdisplaygridlines() {
        return doNotDisplayGridlines;
    }

    public void setDonotdisplaygridlines(String doNotDisplayGridlines) {
        this.doNotDisplayGridlines = doNotDisplayGridlines;
    }
    public String getAllowsizerows() {
        return allowSizeRows;
    }

    public void setAllowsizerows(String allowSizeRows) {
        this.allowSizeRows = allowSizeRows;
    }
    public String getActivecolumn() {
        return activeColumn;
    }

    public void setActivecolumn(String activeColumn) {
        this.activeColumn = activeColumn;
    }
    public String getTabcolorindex() {
        return tabColorIndex;
    }

    public void setTabcolorindex(String tabColorIndex) {
        this.tabColorIndex = tabColorIndex;
    }
    public String getShowpagebreakzoom() {
        return showPageBreakZoom;
    }

    public void setShowpagebreakzoom(String showPageBreakZoom) {
        this.showPageBreakZoom = showPageBreakZoom;
    }
    public String getLeftcolumnrightpane() {
        return leftColumnRightPane;
    }

    public void setLeftcolumnrightpane(String leftColumnRightPane) {
        this.leftColumnRightPane = leftColumnRightPane;
    }
    public String getDonotdisplayheadings() {
        return doNotDisplayHeadings;
    }

    public void setDonotdisplayheadings(String doNotDisplayHeadings) {
        this.doNotDisplayHeadings = doNotDisplayHeadings;
    }
    public String getIntlmacro() {
        return intlMacro;
    }

    public void setIntlmacro(String intlMacro) {
        this.intlMacro = intlMacro;
    }
    public String getNosummarycolumnsrightdetail() {
        return noSummaryColumnsRightDetail;
    }

    public void setNosummarycolumnsrightdetail(String noSummaryColumnsRightDetail) {
        this.noSummaryColumnsRightDetail = noSummaryColumnsRightDetail;
    }
    public String getActivepane() {
        return activePane;
    }

    public void setActivepane(String activePane) {
        this.activePane = activePane;
    }
    public String getDisplayrighttoleft() {
        return displayRightToLeft;
    }

    public void setDisplayrighttoleft(String displayRightToLeft) {
        this.displayRightToLeft = displayRightToLeft;
    }
    public String getSplithorizontal() {
        return splitHorizontal;
    }

    public void setSplithorizontal(String splitHorizontal) {
        this.splitHorizontal = splitHorizontal;
    }
    public String getEnableselection() {
        return enableSelection;
    }

    public void setEnableselection(String enableSelection) {
        this.enableSelection = enableSelection;
    }
    public String getProtectcontentst() {
        return protectContentst;
    }

    public void setProtectcontentst(String protectContentst) {
        this.protectContentst = protectContentst;
    }
    public String getDonotdisplaycolheaders() {
        return doNotDisplayColHeaders;
    }

    public void setDonotdisplaycolheaders(String doNotDisplayColHeaders) {
        this.doNotDisplayColHeaders = doNotDisplayColHeaders;
    }
    public String getProtectobjects() {
        return protectObjects;
    }

    public void setProtectobjects(String protectObjects) {
        this.protectObjects = protectObjects;
    }
    public String getDonotdisplayzeros() {
        return doNotDisplayZeros;
    }

    public void setDonotdisplayzeros(String doNotDisplayZeros) {
        this.doNotDisplayZeros = doNotDisplayZeros;
    }
    public String getAllowinserthyperlinks() {
        return allowInsertHyperlinks;
    }

    public void setAllowinserthyperlinks(String allowInsertHyperlinks) {
        this.allowInsertHyperlinks = allowInsertHyperlinks;
    }
    public String getAllowfilter() {
        return allowFilter;
    }

    public void setAllowfilter(String allowFilter) {
        this.allowFilter = allowFilter;
    }
    public String getFreezepanes() {
        return freezePanes;
    }

    public void setFreezepanes(String freezePanes) {
        this.freezePanes = freezePanes;
    }
    public String getToprowbottompane() {
        return topRowBottomPane;
    }

    public void setToprowbottompane(String topRowBottomPane) {
        this.topRowBottomPane = topRowBottomPane;
    }
    public String getUnsynced() {
        return unsynced;
    }

    public void setUnsynced(String unsynced) {
        this.unsynced = unsynced;
    }
    public String getToprowvisible() {
        return topRowVisible;
    }

    public void setToprowvisible(String topRowVisible) {
        this.topRowVisible = topRowVisible;
    }
    public String getStandardwidth() {
        return standardWidth;
    }

    public void setStandardwidth(String standardWidth) {
        this.standardWidth = standardWidth;
    }
    public String getAllowinsertcols() {
        return allowInsertCols;
    }

    public void setAllowinsertcols(String allowInsertCols) {
        this.allowInsertCols = allowInsertCols;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAllowformatcells() {
        return allowFormatCells;
    }

    public void setAllowformatcells(String allowFormatCells) {
        this.allowFormatCells = allowFormatCells;
    }
    public String getVisible() {
        return visible;
    }

    public void setVisible(String visible) {
        this.visible = visible;
    }

    public Worksheet getWorksheet() {
        return worksheet;
    }

    public void setWorksheet(Worksheet worksheet) {
        this.worksheet = worksheet;
    }

}