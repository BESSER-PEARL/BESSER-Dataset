





import java.util.List;
import java.util.ArrayList;

public class cppmodel_CPPExternalHeader  {

    private String name;





    private cppmodel_CPPExternalHeaderInclusion cppmodel_cppexternalheaderinclusion;


    public cppmodel_CPPExternalHeader(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public cppmodel_CPPExternalHeaderInclusion getCppmodel_cppexternalheaderinclusion() {
        return cppmodel_cppexternalheaderinclusion;
    }

    public void setCppmodel_cppexternalheaderinclusion(cppmodel_CPPExternalHeaderInclusion cppmodel_cppexternalheaderinclusion) {
        this.cppmodel_cppexternalheaderinclusion = cppmodel_cppexternalheaderinclusion;
    }

}