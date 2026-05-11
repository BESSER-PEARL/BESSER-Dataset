





import java.util.List;
import java.util.ArrayList;

public class scxml_Content  {






    private scxml_Invoke scxml_invoke;




    private scxml_Send scxml_send;




    private List<scxml_Content> scxml_contents;




    private scxml_Donedata scxml_donedata;


    public scxml_Content(
    ) {
        this.scxml_contents = new ArrayList<>();
    }

    public scxml_Content(
        ArrayList<scxml_Content> scxml_contents    ) {
        this.scxml_contents = scxml_contents;
    }


    public scxml_Invoke getScxml_invoke() {
        return scxml_invoke;
    }

    public void setScxml_invoke(scxml_Invoke scxml_invoke) {
        this.scxml_invoke = scxml_invoke;
    }
    public scxml_Send getScxml_send() {
        return scxml_send;
    }

    public void setScxml_send(scxml_Send scxml_send) {
        this.scxml_send = scxml_send;
    }
    public List<scxml_Content> getScxml_contents() {
        return scxml_contents;
    }

    public void addScxml_content(Scxml_content scxml_content) {
        this.scxml_contents.add(scxml_content);
    }
    public scxml_Donedata getScxml_donedata() {
        return scxml_donedata;
    }

    public void setScxml_donedata(scxml_Donedata scxml_donedata) {
        this.scxml_donedata = scxml_donedata;
    }

}