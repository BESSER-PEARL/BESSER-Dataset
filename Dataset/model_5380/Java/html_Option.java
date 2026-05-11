





import java.util.List;
import java.util.ArrayList;

public class html_Option  {

    private String content;
    private int value;





    private html_TextArea html_textarea;




    private List<html_FormElement> html_formelements;




    private html_SelectComplex html_selectcomplex;




    private html_Select html_select;


    public html_Option(
        String content,        int value    ) {
        this.content = content;
        this.value = value;
        this.html_formelements = new ArrayList<>();
    }

    public html_Option(
        String content,        int value        ArrayList<html_FormElement> html_formelements    ) {
        this.content = content;
        this.value = value;
        this.html_formelements = html_formelements;
    }

    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }
    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }

    public html_TextArea getHtml_textarea() {
        return html_textarea;
    }

    public void setHtml_textarea(html_TextArea html_textarea) {
        this.html_textarea = html_textarea;
    }
    public List<html_FormElement> getHtml_formelements() {
        return html_formelements;
    }

    public void addHtml_formelement(Html_formelement html_formelement) {
        this.html_formelements.add(html_formelement);
    }
    public html_SelectComplex getHtml_selectcomplex() {
        return html_selectcomplex;
    }

    public void setHtml_selectcomplex(html_SelectComplex html_selectcomplex) {
        this.html_selectcomplex = html_selectcomplex;
    }
    public html_Select getHtml_select() {
        return html_select;
    }

    public void setHtml_select(html_Select html_select) {
        this.html_select = html_select;
    }

}