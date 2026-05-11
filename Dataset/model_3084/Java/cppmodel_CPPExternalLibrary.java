





import java.util.List;
import java.util.ArrayList;

public class cppmodel_CPPExternalLibrary  {






    private List<cppmodel_CPPExternalHeader> cppmodel_cppexternalheaders;


    public cppmodel_CPPExternalLibrary(
    ) {
        this.cppmodel_cppexternalheaders = new ArrayList<>();
    }

    public cppmodel_CPPExternalLibrary(
        ArrayList<cppmodel_CPPExternalHeader> cppmodel_cppexternalheaders    ) {
        this.cppmodel_cppexternalheaders = cppmodel_cppexternalheaders;
    }


    public List<cppmodel_CPPExternalHeader> getCppmodel_cppexternalheaders() {
        return cppmodel_cppexternalheaders;
    }

    public void addCppmodel_cppexternalheader(Cppmodel_cppexternalheader cppmodel_cppexternalheader) {
        this.cppmodel_cppexternalheaders.add(cppmodel_cppexternalheader);
    }

}