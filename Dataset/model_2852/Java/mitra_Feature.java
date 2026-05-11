





import java.util.List;
import java.util.ArrayList;

public class mitra_Feature  {

    private String name;





    private mitra_StaticAccess mitra_staticaccess;




    private mitra_VariableAccess mitra_variableaccess;


    public mitra_Feature(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public mitra_StaticAccess getMitra_staticaccess() {
        return mitra_staticaccess;
    }

    public void setMitra_staticaccess(mitra_StaticAccess mitra_staticaccess) {
        this.mitra_staticaccess = mitra_staticaccess;
    }
    public mitra_VariableAccess getMitra_variableaccess() {
        return mitra_variableaccess;
    }

    public void setMitra_variableaccess(mitra_VariableAccess mitra_variableaccess) {
        this.mitra_variableaccess = mitra_variableaccess;
    }

}