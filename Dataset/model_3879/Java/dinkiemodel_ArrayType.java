





import java.util.List;
import java.util.ArrayList;

public class dinkiemodel_ArrayType extends Type {

    private String arrayType;





    private dinkiemodel_EmptyArrayDecl dinkiemodel_emptyarraydecl;




    private dinkiemodel_FilledArrayDecl dinkiemodel_filledarraydecl;


    public dinkiemodel_ArrayType(
        String arrayType    ) {
        super(
        );
        this.arrayType = arrayType;
    }


    public String getArraytype() {
        return arrayType;
    }

    public void setArraytype(String arrayType) {
        this.arrayType = arrayType;
    }

    public dinkiemodel_EmptyArrayDecl getDinkiemodel_emptyarraydecl() {
        return dinkiemodel_emptyarraydecl;
    }

    public void setDinkiemodel_emptyarraydecl(dinkiemodel_EmptyArrayDecl dinkiemodel_emptyarraydecl) {
        this.dinkiemodel_emptyarraydecl = dinkiemodel_emptyarraydecl;
    }
    public dinkiemodel_FilledArrayDecl getDinkiemodel_filledarraydecl() {
        return dinkiemodel_filledarraydecl;
    }

    public void setDinkiemodel_filledarraydecl(dinkiemodel_FilledArrayDecl dinkiemodel_filledarraydecl) {
        this.dinkiemodel_filledarraydecl = dinkiemodel_filledarraydecl;
    }

}