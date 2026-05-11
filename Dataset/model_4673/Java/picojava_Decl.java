





import java.util.List;
import java.util.ArrayList;

public class picojava_Decl extends BlockStmt {

    private String Name;
    private boolean isUnknown;





    private picojava_Block picojava_block;




    private picojava_TypeDecl picojava_typedecl;




    private picojava_TypeDecl picojava_typedecl;




    private picojava_PrimitiveDecl picojava_primitivedecl;


    public picojava_Decl(
        String Name,        boolean isUnknown    ) {
        super(
        );
        this.Name = Name;
        this.isUnknown = isUnknown;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public boolean getIsunknown() {
        return isUnknown;
    }

    public void setIsunknown(boolean isUnknown) {
        this.isUnknown = isUnknown;
    }

    public picojava_Block getPicojava_block() {
        return picojava_block;
    }

    public void setPicojava_block(picojava_Block picojava_block) {
        this.picojava_block = picojava_block;
    }
    public picojava_TypeDecl getPicojava_typedecl() {
        return picojava_typedecl;
    }

    public void setPicojava_typedecl(picojava_TypeDecl picojava_typedecl) {
        this.picojava_typedecl = picojava_typedecl;
    }
    public picojava_TypeDecl getPicojava_typedecl() {
        return picojava_typedecl;
    }

    public void setPicojava_typedecl(picojava_TypeDecl picojava_typedecl) {
        this.picojava_typedecl = picojava_typedecl;
    }
    public picojava_PrimitiveDecl getPicojava_primitivedecl() {
        return picojava_primitivedecl;
    }

    public void setPicojava_primitivedecl(picojava_PrimitiveDecl picojava_primitivedecl) {
        this.picojava_primitivedecl = picojava_primitivedecl;
    }

}