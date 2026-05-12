





import java.util.List;
import java.util.ArrayList;

public class SpreadsheetMLPrintingSetup_Print  {

    private String printErrors;
    private String fitHeight;
    private String validPrinterInfo;
    private String leftToRight;
    private String blackAndWhite;
    private String verticalResolution;
    private String scale;
    private String horizontalResolution;
    private String commentsLayout;
    private String numberOfCopies;
    private String gridlines;
    private String rowColHeadings;
    private String paperSizeIndex;
    private String fitWidth;
    private String draftQuality;





    private WorksheetOptionsElt worksheetoptionselt;


    public SpreadsheetMLPrintingSetup_Print(
        String printErrors,        String fitHeight,        String validPrinterInfo,        String leftToRight,        String blackAndWhite,        String verticalResolution,        String scale,        String horizontalResolution,        String commentsLayout,        String numberOfCopies,        String gridlines,        String rowColHeadings,        String paperSizeIndex,        String fitWidth,        String draftQuality    ) {
        this.printErrors = printErrors;
        this.fitHeight = fitHeight;
        this.validPrinterInfo = validPrinterInfo;
        this.leftToRight = leftToRight;
        this.blackAndWhite = blackAndWhite;
        this.verticalResolution = verticalResolution;
        this.scale = scale;
        this.horizontalResolution = horizontalResolution;
        this.commentsLayout = commentsLayout;
        this.numberOfCopies = numberOfCopies;
        this.gridlines = gridlines;
        this.rowColHeadings = rowColHeadings;
        this.paperSizeIndex = paperSizeIndex;
        this.fitWidth = fitWidth;
        this.draftQuality = draftQuality;
    }


    public String getPrinterrors() {
        return printErrors;
    }

    public void setPrinterrors(String printErrors) {
        this.printErrors = printErrors;
    }
    public String getFitheight() {
        return fitHeight;
    }

    public void setFitheight(String fitHeight) {
        this.fitHeight = fitHeight;
    }
    public String getValidprinterinfo() {
        return validPrinterInfo;
    }

    public void setValidprinterinfo(String validPrinterInfo) {
        this.validPrinterInfo = validPrinterInfo;
    }
    public String getLefttoright() {
        return leftToRight;
    }

    public void setLefttoright(String leftToRight) {
        this.leftToRight = leftToRight;
    }
    public String getBlackandwhite() {
        return blackAndWhite;
    }

    public void setBlackandwhite(String blackAndWhite) {
        this.blackAndWhite = blackAndWhite;
    }
    public String getVerticalresolution() {
        return verticalResolution;
    }

    public void setVerticalresolution(String verticalResolution) {
        this.verticalResolution = verticalResolution;
    }
    public String getScale() {
        return scale;
    }

    public void setScale(String scale) {
        this.scale = scale;
    }
    public String getHorizontalresolution() {
        return horizontalResolution;
    }

    public void setHorizontalresolution(String horizontalResolution) {
        this.horizontalResolution = horizontalResolution;
    }
    public String getCommentslayout() {
        return commentsLayout;
    }

    public void setCommentslayout(String commentsLayout) {
        this.commentsLayout = commentsLayout;
    }
    public String getNumberofcopies() {
        return numberOfCopies;
    }

    public void setNumberofcopies(String numberOfCopies) {
        this.numberOfCopies = numberOfCopies;
    }
    public String getGridlines() {
        return gridlines;
    }

    public void setGridlines(String gridlines) {
        this.gridlines = gridlines;
    }
    public String getRowcolheadings() {
        return rowColHeadings;
    }

    public void setRowcolheadings(String rowColHeadings) {
        this.rowColHeadings = rowColHeadings;
    }
    public String getPapersizeindex() {
        return paperSizeIndex;
    }

    public void setPapersizeindex(String paperSizeIndex) {
        this.paperSizeIndex = paperSizeIndex;
    }
    public String getFitwidth() {
        return fitWidth;
    }

    public void setFitwidth(String fitWidth) {
        this.fitWidth = fitWidth;
    }
    public String getDraftquality() {
        return draftQuality;
    }

    public void setDraftquality(String draftQuality) {
        this.draftQuality = draftQuality;
    }

    public WorksheetOptionsElt getWorksheetoptionselt() {
        return worksheetoptionselt;
    }

    public void setWorksheetoptionselt(WorksheetOptionsElt worksheetoptionselt) {
        this.worksheetoptionselt = worksheetoptionselt;
    }

}