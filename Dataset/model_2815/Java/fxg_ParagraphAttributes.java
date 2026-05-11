





import java.util.List;
import java.util.ArrayList;

public class fxg_ParagraphAttributes  {

    private String justificationStyle;
    private String paragraphSpaceAfter;
    private String tabStops;
    private String paragraphSpaceBefore;
    private String textAlign;
    private String paragraphStartIndent;
    private String leadingModel;
    private String textIndent;
    private String justificationRule;
    private String textAlignLast;
    private String textJustify;
    private String paragraphEndIndent;



    public fxg_ParagraphAttributes(
        String justificationStyle,        String paragraphSpaceAfter,        String tabStops,        String paragraphSpaceBefore,        String textAlign,        String paragraphStartIndent,        String leadingModel,        String textIndent,        String justificationRule,        String textAlignLast,        String textJustify,        String paragraphEndIndent    ) {
        this.justificationStyle = justificationStyle;
        this.paragraphSpaceAfter = paragraphSpaceAfter;
        this.tabStops = tabStops;
        this.paragraphSpaceBefore = paragraphSpaceBefore;
        this.textAlign = textAlign;
        this.paragraphStartIndent = paragraphStartIndent;
        this.leadingModel = leadingModel;
        this.textIndent = textIndent;
        this.justificationRule = justificationRule;
        this.textAlignLast = textAlignLast;
        this.textJustify = textJustify;
        this.paragraphEndIndent = paragraphEndIndent;
    }


    public String getJustificationstyle() {
        return justificationStyle;
    }

    public void setJustificationstyle(String justificationStyle) {
        this.justificationStyle = justificationStyle;
    }
    public String getParagraphspaceafter() {
        return paragraphSpaceAfter;
    }

    public void setParagraphspaceafter(String paragraphSpaceAfter) {
        this.paragraphSpaceAfter = paragraphSpaceAfter;
    }
    public String getTabstops() {
        return tabStops;
    }

    public void setTabstops(String tabStops) {
        this.tabStops = tabStops;
    }
    public String getParagraphspacebefore() {
        return paragraphSpaceBefore;
    }

    public void setParagraphspacebefore(String paragraphSpaceBefore) {
        this.paragraphSpaceBefore = paragraphSpaceBefore;
    }
    public String getTextalign() {
        return textAlign;
    }

    public void setTextalign(String textAlign) {
        this.textAlign = textAlign;
    }
    public String getParagraphstartindent() {
        return paragraphStartIndent;
    }

    public void setParagraphstartindent(String paragraphStartIndent) {
        this.paragraphStartIndent = paragraphStartIndent;
    }
    public String getLeadingmodel() {
        return leadingModel;
    }

    public void setLeadingmodel(String leadingModel) {
        this.leadingModel = leadingModel;
    }
    public String getTextindent() {
        return textIndent;
    }

    public void setTextindent(String textIndent) {
        this.textIndent = textIndent;
    }
    public String getJustificationrule() {
        return justificationRule;
    }

    public void setJustificationrule(String justificationRule) {
        this.justificationRule = justificationRule;
    }
    public String getTextalignlast() {
        return textAlignLast;
    }

    public void setTextalignlast(String textAlignLast) {
        this.textAlignLast = textAlignLast;
    }
    public String getTextjustify() {
        return textJustify;
    }

    public void setTextjustify(String textJustify) {
        this.textJustify = textJustify;
    }
    public String getParagraphendindent() {
        return paragraphEndIndent;
    }

    public void setParagraphendindent(String paragraphEndIndent) {
        this.paragraphEndIndent = paragraphEndIndent;
    }


}