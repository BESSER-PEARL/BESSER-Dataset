





import java.util.List;
import java.util.ArrayList;

public class brmodel_Method extends Trace {

    private String class_;
    private String name;



    public brmodel_Method(
        String class_,        String name    ) {
        super(
        );
        this.class_ = class_;
        this.name = name;
    }


    public String getClass_() {
        return class_;
    }

    public void setClass_(String class_) {
        this.class_ = class_;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}