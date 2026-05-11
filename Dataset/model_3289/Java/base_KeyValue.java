





import java.util.List;
import java.util.ArrayList;

public class base_KeyValue  {

    private String key;





    private base_Annotation base_annotation;




    private base_Literal base_literal;


    public base_KeyValue(
        String key    ) {
        this.key = key;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public base_Annotation getBase_annotation() {
        return base_annotation;
    }

    public void setBase_annotation(base_Annotation base_annotation) {
        this.base_annotation = base_annotation;
    }
    public base_Literal getBase_literal() {
        return base_literal;
    }

    public void setBase_literal(base_Literal base_literal) {
        this.base_literal = base_literal;
    }

}