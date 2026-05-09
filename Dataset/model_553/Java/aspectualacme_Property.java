





import java.util.List;
import java.util.ArrayList;

public class aspectualacme_Property  {

    private String name;
    private String value;





    private aspectualacme_Element aspectualacme_element;


    public aspectualacme_Property(
        String name,        String value    ) {
        this.name = name;
        this.value = value;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public aspectualacme_Element getAspectualacme_element() {
        return aspectualacme_element;
    }

    public void setAspectualacme_element(aspectualacme_Element aspectualacme_element) {
        this.aspectualacme_element = aspectualacme_element;
    }

}