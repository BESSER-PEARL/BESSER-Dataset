





import java.util.List;
import java.util.ArrayList;

public class dom_InClass extends FromRange {

    private String name;
    private String class_;



    public dom_InClass(
        String name,        String class_    ) {
        super(
        );
        this.name = name;
        this.class_ = class_;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getClass_() {
        return class_;
    }

    public void setClass_(String class_) {
        this.class_ = class_;
    }


}