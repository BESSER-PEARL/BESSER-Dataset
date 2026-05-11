





import java.util.List;
import java.util.ArrayList;

public class idl_FileName  {

    private String name;





    private idl_Preproc_Include idl_preproc_include;


    public idl_FileName(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public idl_Preproc_Include getIdl_preproc_include() {
        return idl_preproc_include;
    }

    public void setIdl_preproc_include(idl_Preproc_Include idl_preproc_include) {
        this.idl_preproc_include = idl_preproc_include;
    }

}