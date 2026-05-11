





import java.util.List;
import java.util.ArrayList;

public class fxg_ParagraphAttributes  {

    private String tabStops;
    private String textAlignLast;
    private String textAlign;
    private String textIndent;
    private String justificationRule;
    private String paragraphEndIndent;
    private String paragraphSpaceBefore;
    private String justificationStyle;
    private String paragraphSpaceAfter;
    private String leadingModel;
    private String paragraphStartIndent;
    private String textJustify;



    public fxg_ParagraphAttributes(
        String tabStops,        String textAlignLast,        String textAlign,        String textIndent,        String justificationRule,        String paragraphEndIndent,        String paragraphSpaceBefore,        String justificationStyle,        String paragraphSpaceAfter,        String leadingModel,        String paragraphStartIndent,        String textJustify    ) {
        this.tabStops = tabStops;
        this.textAlignLast = textAlignLast;
        this.textAlign = textAlign;
        this.textIndent = textIndent;
        this.justificationRule = justificationRule;
        this.paragraphEndIndent = paragraphEndIndent;
        this.paragraphSpaceBefore = paragraphSpaceBefore;
        this.justificationStyle = justificationStyle;
        this.paragraphSpaceAfter = paragraphSpaceAfter;
        this.leadingModel = leadingModel;
        this.paragraphStartIndent = paragraphStartIndent;
        this.textJustify = textJustify;
    }


    public String getTabstops() {
        return tabStops;
    }

    public void setTabstops(String tabStops) {
        this.tabStops = tabStops;
    }
    public String getTextalignlast() {
        return textAlignLast;
    }

    public void setTextalignlast(String textAlignLast) {
        this.textAlignLast = textAlignLast;
    }
    public String getTextalign() {
        return textAlign;
    }

    public void setTextalign(String textAlign) {
        this.textAlign = textAlign;
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
    public String getParagraphendindent() {
        return paragraphEndIndent;
    }

    public void setParagraphendindent(String paragraphEndIndent) {
        this.paragraphEndIndent = paragraphEndIndent;
    }
    public String getParagraphspacebefore() {
        return paragraphSpaceBefore;
    }

    public void setParagraphspacebefore(String paragraphSpaceBefore) {
        this.paragraphSpaceBefore = paragraphSpaceBefore;
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
    public String getLeadingmodel() {
        return leadingModel;
    }

    public void setLeadingmodel(String leadingModel) {
        this.leadingModel = leadingModel;
    }
    public String getParagraphstartindent() {
        return paragraphStartIndent;
    }

    public void setParagraphstartindent(String paragraphStartIndent) {
        this.paragraphStartIndent = paragraphStartIndent;
    }
    public String getTextjustify() {
        return textJustify;
    }

    public void setTextjustify(String textJustify) {
        this.textJustify = textJustify;
    }


}