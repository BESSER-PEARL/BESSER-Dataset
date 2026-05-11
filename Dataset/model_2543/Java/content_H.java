





import java.util.List;
import java.util.ArrayList;

public class content_H  {






    private List<content_R> content_rs;




    private content_E content_e;




    private content_Q content_q;


    public content_H(
    ) {
        this.content_rs = new ArrayList<>();
    }

    public content_H(
        ArrayList<content_R> content_rs    ) {
        this.content_rs = content_rs;
    }


    public List<content_R> getContent_rs() {
        return content_rs;
    }

    public void addContent_r(Content_r content_r) {
        this.content_rs.add(content_r);
    }
    public content_E getContent_e() {
        return content_e;
    }

    public void setContent_e(content_E content_e) {
        this.content_e = content_e;
    }
    public content_Q getContent_q() {
        return content_q;
    }

    public void setContent_q(content_Q content_q) {
        this.content_q = content_q;
    }

}