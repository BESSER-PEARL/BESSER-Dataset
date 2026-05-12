





import java.util.List;
import java.util.ArrayList;

public class SpreadsheetMLStyles_Print  {

    private String rowColHeadings;
    private String validPrinterInfo;
    private String commentsLayout;
    private String blackAndWhite;
    private String fitHeight;
    private String printErrors;
    private String horizontalResolution;
    private String verticalResolution;
    private String paperSizeIndex;
    private String fitWidth;
    private String scale;
    private String numberOfCopies;
    private String gridlines;
    private String leftToRight;
    private String draftQuality;





    private WorksheetOptionsElt worksheetoptionselt;


    public SpreadsheetMLStyles_Print(
        String rowColHeadings,        String validPrinterInfo,        String commentsLayout,        String blackAndWhite,        String fitHeight,        String printErrors,        String horizontalResolution,        String verticalResolution,        String paperSizeIndex,        String fitWidth,        String scale,        String numberOfCopies,        String gridlines,        String leftToRight,        String draftQuality    ) {
        this.rowColHeadings = rowColHeadings;
        this.validPrinterInfo = validPrinterInfo;
        this.commentsLayout = commentsLayout;
        this.blackAndWhite = blackAndWhite;
        this.fitHeight = fitHeight;
        this.printErrors = printErrors;
        this.horizontalResolution = horizontalResolution;
        this.verticalResolution = verticalResolution;
        this.paperSizeIndex = paperSizeIndex;
        this.fitWidth = fitWidth;
        this.scale = scale;
        this.numberOfCopies = numberOfCopies;
        this.gridlines = gridlines;
        this.leftToRight = leftToRight;
        this.draftQuality = draftQuality;
    }


    public String getRowcolheadings() {
        return rowColHeadings;
    }

    public void setRowcolheadings(String rowColHeadings) {
        this.rowColHeadings = rowColHeadings;
    }
    public String getValidprinterinfo() {
        return validPrinterInfo;
    }

    public void setValidprinterinfo(String validPrinterInfo) {
        this.validPrinterInfo = validPrinterInfo;
    }
    public String getCommentslayout() {
        return commentsLayout;
    }

    public void setCommentslayout(String commentsLayout) {
        this.commentsLayout = commentsLayout;
    }
    public String getBlackandwhite() {
        return blackAndWhite;
    }

    public void setBlackandwhite(String blackAndWhite) {
        this.blackAndWhite = blackAndWhite;
    }
    public String getFitheight() {
        return fitHeight;
    }

    public void setFitheight(String fitHeight) {
        this.fitHeight = fitHeight;
    }
    public String getPrinterrors() {
        return printErrors;
    }

    public void setPrinterrors(String printErrors) {
        this.printErrors = printErrors;
    }
    public String getHorizontalresolution() {
        return horizontalResolution;
    }

    public void setHorizontalresolution(String horizontalResolution) {
        this.horizontalResolution = horizontalResolution;
    }
    public String getVerticalresolution() {
        return verticalResolution;
    }

    public void setVerticalresolution(String verticalResolution) {
        this.verticalResolution = verticalResolution;
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
    public String getScale() {
        return scale;
    }

    public void setScale(String scale) {
        this.scale = scale;
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
    public String getLefttoright() {
        return leftToRight;
    }

    public void setLefttoright(String leftToRight) {
        this.leftToRight = leftToRight;
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