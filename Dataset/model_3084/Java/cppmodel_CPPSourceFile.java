





import java.util.List;
import java.util.ArrayList;

public class cppmodel_CPPSourceFile  {

    private String generationName;
    private String generationPath;
    private String generationDirectory;





    private List<cppmodel_CPPHeaderFile> cppmodel_cppheaderfiles;




    private cppmodel_CPPDirectory cppmodel_cppdirectory;


    public cppmodel_CPPSourceFile(
        String generationName,        String generationPath,        String generationDirectory    ) {
        this.generationName = generationName;
        this.generationPath = generationPath;
        this.generationDirectory = generationDirectory;
        this.cppmodel_cppheaderfiles = new ArrayList<>();
    }

    public cppmodel_CPPSourceFile(
        String generationName,        String generationPath,        String generationDirectory        ArrayList<cppmodel_CPPHeaderFile> cppmodel_cppheaderfiles    ) {
        this.generationName = generationName;
        this.generationPath = generationPath;
        this.generationDirectory = generationDirectory;
        this.cppmodel_cppheaderfiles = cppmodel_cppheaderfiles;
    }

    public String getGenerationname() {
        return generationName;
    }

    public void setGenerationname(String generationName) {
        this.generationName = generationName;
    }
    public String getGenerationpath() {
        return generationPath;
    }

    public void setGenerationpath(String generationPath) {
        this.generationPath = generationPath;
    }
    public String getGenerationdirectory() {
        return generationDirectory;
    }

    public void setGenerationdirectory(String generationDirectory) {
        this.generationDirectory = generationDirectory;
    }

    public List<cppmodel_CPPHeaderFile> getCppmodel_cppheaderfiles() {
        return cppmodel_cppheaderfiles;
    }

    public void addCppmodel_cppheaderfile(Cppmodel_cppheaderfile cppmodel_cppheaderfile) {
        this.cppmodel_cppheaderfiles.add(cppmodel_cppheaderfile);
    }
    public cppmodel_CPPDirectory getCppmodel_cppdirectory() {
        return cppmodel_cppdirectory;
    }

    public void setCppmodel_cppdirectory(cppmodel_CPPDirectory cppmodel_cppdirectory) {
        this.cppmodel_cppdirectory = cppmodel_cppdirectory;
    }

}