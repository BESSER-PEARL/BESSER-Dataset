





import java.util.List;
import java.util.ArrayList;

public class vhdl_declaration_AttributeSpecification extends Named, declaration_Declaration {

    private String class_;



    public vhdl_declaration_AttributeSpecification(
        String class_    ) {
        super(
        );
        this.class_ = class_;
    }


    public String getClass_() {
        return class_;
    }

    public void setClass_(String class_) {
        this.class_ = class_;
    }


}