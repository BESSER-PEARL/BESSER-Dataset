





import java.util.List;
import java.util.ArrayList;

public class picojava_IdUse extends Access {

    private String Name;
    private boolean isQualified;





    private picojava_Access picojava_access;




    private picojava_ClassDecl picojava_classdecl;


    public picojava_IdUse(
        String Name,        boolean isQualified    ) {
        super(
        );
        this.Name = Name;
        this.isQualified = isQualified;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public boolean getIsqualified() {
        return isQualified;
    }

    public void setIsqualified(boolean isQualified) {
        this.isQualified = isQualified;
    }

    public picojava_Access getPicojava_access() {
        return picojava_access;
    }

    public void setPicojava_access(picojava_Access picojava_access) {
        this.picojava_access = picojava_access;
    }
    public picojava_ClassDecl getPicojava_classdecl() {
        return picojava_classdecl;
    }

    public void setPicojava_classdecl(picojava_ClassDecl picojava_classdecl) {
        this.picojava_classdecl = picojava_classdecl;
    }

}