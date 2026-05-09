





import java.util.List;
import java.util.ArrayList;

public class vhdl_AttributeSpecification extends BlockDeclarativeItem {

    private String entity;
    private String class_;
    private String name;





    private vhdl_Expression vhdl_expression;


    public vhdl_AttributeSpecification(
        String entity,        String class_,        String name    ) {
        super(
        );
        this.entity = entity;
        this.class_ = class_;
        this.name = name;
    }


    public String getEntity() {
        return entity;
    }

    public void setEntity(String entity) {
        this.entity = entity;
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

    public vhdl_Expression getVhdl_expression() {
        return vhdl_expression;
    }

    public void setVhdl_expression(vhdl_Expression vhdl_expression) {
        this.vhdl_expression = vhdl_expression;
    }

}