





import java.util.List;
import java.util.ArrayList;

public class content_G  {






    private List<content_H> content_hs;




    private List<content_I> content_is;




    private content_C content_c;




    private List<content_Q> content_qs;


    public content_G(
    ) {
        this.content_hs = new ArrayList<>();
        this.content_is = new ArrayList<>();
        this.content_qs = new ArrayList<>();
    }

    public content_G(
        ArrayList<content_H> content_hs,        ArrayList<content_I> content_is,        ArrayList<content_Q> content_qs    ) {
        this.content_hs = content_hs;
        this.content_is = content_is;
        this.content_qs = content_qs;
    }


    public List<content_H> getContent_hs() {
        return content_hs;
    }

    public void addContent_h(Content_h content_h) {
        this.content_hs.add(content_h);
    }
    public List<content_I> getContent_is() {
        return content_is;
    }

    public void addContent_i(Content_i content_i) {
        this.content_is.add(content_i);
    }
    public content_C getContent_c() {
        return content_c;
    }

    public void setContent_c(content_C content_c) {
        this.content_c = content_c;
    }
    public List<content_Q> getContent_qs() {
        return content_qs;
    }

    public void addContent_q(Content_q content_q) {
        this.content_qs.add(content_q);
    }

}