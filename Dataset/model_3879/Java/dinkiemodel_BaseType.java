





import java.util.List;
import java.util.ArrayList;

public class dinkiemodel_BaseType extends Type {

    private String type;





    private dinkiemodel_Declaration dinkiemodel_declaration;




    private dinkiemodel_ReadStatement dinkiemodel_readstatement;


    public dinkiemodel_BaseType(
        String type    ) {
        super(
        );
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public dinkiemodel_Declaration getDinkiemodel_declaration() {
        return dinkiemodel_declaration;
    }

    public void setDinkiemodel_declaration(dinkiemodel_Declaration dinkiemodel_declaration) {
        this.dinkiemodel_declaration = dinkiemodel_declaration;
    }
    public dinkiemodel_ReadStatement getDinkiemodel_readstatement() {
        return dinkiemodel_readstatement;
    }

    public void setDinkiemodel_readstatement(dinkiemodel_ReadStatement dinkiemodel_readstatement) {
        this.dinkiemodel_readstatement = dinkiemodel_readstatement;
    }

}