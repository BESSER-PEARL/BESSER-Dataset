





import java.util.List;
import java.util.ArrayList;

public class content_A  {






    private List<content_C> content_cs;




    private content_A content_a;




    private List<content_D> content_ds;




    private List<content_F> content_fs;




    private List<content_E> content_es;


    public content_A(
    ) {
        this.content_cs = new ArrayList<>();
        this.content_ds = new ArrayList<>();
        this.content_fs = new ArrayList<>();
        this.content_es = new ArrayList<>();
    }

    public content_A(
        ArrayList<content_C> content_cs,        ArrayList<content_D> content_ds,        ArrayList<content_F> content_fs,        ArrayList<content_E> content_es    ) {
        this.content_cs = content_cs;
        this.content_ds = content_ds;
        this.content_fs = content_fs;
        this.content_es = content_es;
    }


    public List<content_C> getContent_cs() {
        return content_cs;
    }

    public void addContent_c(Content_c content_c) {
        this.content_cs.add(content_c);
    }
    public content_A getContent_a() {
        return content_a;
    }

    public void setContent_a(content_A content_a) {
        this.content_a = content_a;
    }
    public List<content_D> getContent_ds() {
        return content_ds;
    }

    public void addContent_d(Content_d content_d) {
        this.content_ds.add(content_d);
    }
    public List<content_F> getContent_fs() {
        return content_fs;
    }

    public void addContent_f(Content_f content_f) {
        this.content_fs.add(content_f);
    }
    public List<content_E> getContent_es() {
        return content_es;
    }

    public void addContent_e(Content_e content_e) {
        this.content_es.add(content_e);
    }

}