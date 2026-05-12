





import java.util.List;
import java.util.ArrayList;

public class WordprocessingMLStyles_ParaPrElt  {

    private None bidi;
    private None justification;
    private None suppressAutoHyphens;
    private None keepNext;
    private None pageBreakBefore;
    private None supressLineNumbers;
    private None contextualSpacing;
    private None keepLines;





    private StringProperty stringproperty;


    public WordprocessingMLStyles_ParaPrElt(
        None bidi,        None justification,        None suppressAutoHyphens,        None keepNext,        None pageBreakBefore,        None supressLineNumbers,        None contextualSpacing,        None keepLines    ) {
        this.bidi = bidi;
        this.justification = justification;
        this.suppressAutoHyphens = suppressAutoHyphens;
        this.keepNext = keepNext;
        this.pageBreakBefore = pageBreakBefore;
        this.supressLineNumbers = supressLineNumbers;
        this.contextualSpacing = contextualSpacing;
        this.keepLines = keepLines;
    }


    public None getBidi() {
        return bidi;
    }

    public void setBidi(None bidi) {
        this.bidi = bidi;
    }
    public None getJustification() {
        return justification;
    }

    public void setJustification(None justification) {
        this.justification = justification;
    }
    public None getSuppressautohyphens() {
        return suppressAutoHyphens;
    }

    public void setSuppressautohyphens(None suppressAutoHyphens) {
        this.suppressAutoHyphens = suppressAutoHyphens;
    }
    public None getKeepnext() {
        return keepNext;
    }

    public void setKeepnext(None keepNext) {
        this.keepNext = keepNext;
    }
    public None getPagebreakbefore() {
        return pageBreakBefore;
    }

    public void setPagebreakbefore(None pageBreakBefore) {
        this.pageBreakBefore = pageBreakBefore;
    }
    public None getSupresslinenumbers() {
        return supressLineNumbers;
    }

    public void setSupresslinenumbers(None supressLineNumbers) {
        this.supressLineNumbers = supressLineNumbers;
    }
    public None getContextualspacing() {
        return contextualSpacing;
    }

    public void setContextualspacing(None contextualSpacing) {
        this.contextualSpacing = contextualSpacing;
    }
    public None getKeeplines() {
        return keepLines;
    }

    public void setKeeplines(None keepLines) {
        this.keepLines = keepLines;
    }

    public StringProperty getStringproperty() {
        return stringproperty;
    }

    public void setStringproperty(StringProperty stringproperty) {
        this.stringproperty = stringproperty;
    }

}