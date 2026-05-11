





import java.util.List;
import java.util.ArrayList;

public class content_J  {

    private String linkName;
    private int cardinality;





    private content_F content_f;




    private content_H content_h;


    public content_J(
        String linkName,        int cardinality    ) {
        this.linkName = linkName;
        this.cardinality = cardinality;
    }


    public String getLinkname() {
        return linkName;
    }

    public void setLinkname(String linkName) {
        this.linkName = linkName;
    }
    public int getCardinality() {
        return cardinality;
    }

    public void setCardinality(int cardinality) {
        this.cardinality = cardinality;
    }

    public content_F getContent_f() {
        return content_f;
    }

    public void setContent_f(content_F content_f) {
        this.content_f = content_f;
    }
    public content_H getContent_h() {
        return content_h;
    }

    public void setContent_h(content_H content_h) {
        this.content_h = content_h;
    }

}