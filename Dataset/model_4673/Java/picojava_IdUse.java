





import java.util.List;
import java.util.ArrayList;

public class picojava_IdUse extends Access {

    private boolean isQualified;
    private String Name;





    private picojava_ClassDecl picojava_classdecl;




    private picojava_Access picojava_access;


    public picojava_IdUse(
        boolean isQualified,        String Name    ) {
        super(
        );
        this.isQualified = isQualified;
        this.Name = Name;
    }


    public boolean getIsqualified() {
        return isQualified;
    }

    public void setIsqualified(boolean isQualified) {
        this.isQualified = isQualified;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public picojava_ClassDecl getPicojava_classdecl() {
        return picojava_classdecl;
    }

    public void setPicojava_classdecl(picojava_ClassDecl picojava_classdecl) {
        this.picojava_classdecl = picojava_classdecl;
    }
    public picojava_Access getPicojava_access() {
        return picojava_access;
    }

    public void setPicojava_access(picojava_Access picojava_access) {
        this.picojava_access = picojava_access;
    }

}