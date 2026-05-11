





import java.util.List;
import java.util.ArrayList;

public class picojava_ClassDecl extends TypeDecl {

    private boolean hasCycleOnSuperclassChain;





    private picojava_ClassDecl picojava_classdecl;




    private picojava_Block picojava_block;


    public picojava_ClassDecl(
        boolean hasCycleOnSuperclassChain    ) {
        super(
        );
        this.hasCycleOnSuperclassChain = hasCycleOnSuperclassChain;
    }


    public boolean getHascycleonsuperclasschain() {
        return hasCycleOnSuperclassChain;
    }

    public void setHascycleonsuperclasschain(boolean hasCycleOnSuperclassChain) {
        this.hasCycleOnSuperclassChain = hasCycleOnSuperclassChain;
    }

    public picojava_ClassDecl getPicojava_classdecl() {
        return picojava_classdecl;
    }

    public void setPicojava_classdecl(picojava_ClassDecl picojava_classdecl) {
        this.picojava_classdecl = picojava_classdecl;
    }
    public picojava_Block getPicojava_block() {
        return picojava_block;
    }

    public void setPicojava_block(picojava_Block picojava_block) {
        this.picojava_block = picojava_block;
    }

}