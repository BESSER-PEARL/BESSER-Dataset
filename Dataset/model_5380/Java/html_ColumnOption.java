





import java.util.List;
import java.util.ArrayList;

public class html_ColumnOption  {

    private String content;
    private int value;





    private html_SelectComplex html_selectcomplex;


    public html_ColumnOption(
        String content,        int value    ) {
        this.content = content;
        this.value = value;
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

    public html_SelectComplex getHtml_selectcomplex() {
        return html_selectcomplex;
    }

    public void setHtml_selectcomplex(html_SelectComplex html_selectcomplex) {
        this.html_selectcomplex = html_selectcomplex;
    }

}