





import java.util.List;
import java.util.ArrayList;

public class alldatatypes_Strings extends Type {

    private String text_01;
    private String text_01_EmptyDefault;
    private String textarea;
    private String text_1;
    private String link_01;
    private String html_01;
    private String notEditableText_01;



    public alldatatypes_Strings(
        String text_01,        String text_01_EmptyDefault,        String textarea,        String text_1,        String link_01,        String html_01,        String notEditableText_01    ) {
        super(
        );
        this.text_01 = text_01;
        this.text_01_EmptyDefault = text_01_EmptyDefault;
        this.textarea = textarea;
        this.text_1 = text_1;
        this.link_01 = link_01;
        this.html_01 = html_01;
        this.notEditableText_01 = notEditableText_01;
    }


    public String getText_01() {
        return text_01;
    }

    public void setText_01(String text_01) {
        this.text_01 = text_01;
    }
    public String getText_01_emptydefault() {
        return text_01_EmptyDefault;
    }

    public void setText_01_emptydefault(String text_01_EmptyDefault) {
        this.text_01_EmptyDefault = text_01_EmptyDefault;
    }
    public String getTextarea() {
        return textarea;
    }

    public void setTextarea(String textarea) {
        this.textarea = textarea;
    }
    public String getText_1() {
        return text_1;
    }

    public void setText_1(String text_1) {
        this.text_1 = text_1;
    }
    public String getLink_01() {
        return link_01;
    }

    public void setLink_01(String link_01) {
        this.link_01 = link_01;
    }
    public String getHtml_01() {
        return html_01;
    }

    public void setHtml_01(String html_01) {
        this.html_01 = html_01;
    }
    public String getNoteditabletext_01() {
        return notEditableText_01;
    }

    public void setNoteditabletext_01(String notEditableText_01) {
        this.notEditableText_01 = notEditableText_01;
    }


}