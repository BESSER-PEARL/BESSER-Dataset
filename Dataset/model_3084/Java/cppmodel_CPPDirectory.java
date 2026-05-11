





import java.util.List;
import java.util.ArrayList;

public class cppmodel_CPPDirectory  {

    private String path;
    private String name;
    private String parentDirectory;





    private cppmodel_CPPComponent cppmodel_cppcomponent;




    private List<cppmodel_CPPDirectory> cppmodel_cppdirectorys;




    private cppmodel_CPPPackage cppmodel_cpppackage;




    private cppmodel_CPPModel cppmodel_cppmodel;




    private cppmodel_CPPModel cppmodel_cppmodel;




    private cppmodel_CPPPackage cppmodel_cpppackage;




    private cppmodel_CPPComponent cppmodel_cppcomponent;




    private cppmodel_CPPComponent cppmodel_cppcomponent;




    private cppmodel_CPPComponent cppmodel_cppcomponent;




    private cppmodel_CPPModel cppmodel_cppmodel;




    private cppmodel_CPPModel cppmodel_cppmodel;


    public cppmodel_CPPDirectory(
        String path,        String name,        String parentDirectory    ) {
        this.path = path;
        this.name = name;
        this.parentDirectory = parentDirectory;
        this.cppmodel_cppdirectorys = new ArrayList<>();
    }

    public cppmodel_CPPDirectory(
        String path,        String name,        String parentDirectory        ArrayList<cppmodel_CPPDirectory> cppmodel_cppdirectorys    ) {
        this.path = path;
        this.name = name;
        this.parentDirectory = parentDirectory;
        this.cppmodel_cppdirectorys = cppmodel_cppdirectorys;
    }

    public String getPath() {
        return path;
    }

    public void setPath(String path) {
        this.path = path;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getParentdirectory() {
        return parentDirectory;
    }

    public void setParentdirectory(String parentDirectory) {
        this.parentDirectory = parentDirectory;
    }

    public cppmodel_CPPComponent getCppmodel_cppcomponent() {
        return cppmodel_cppcomponent;
    }

    public void setCppmodel_cppcomponent(cppmodel_CPPComponent cppmodel_cppcomponent) {
        this.cppmodel_cppcomponent = cppmodel_cppcomponent;
    }
    public List<cppmodel_CPPDirectory> getCppmodel_cppdirectorys() {
        return cppmodel_cppdirectorys;
    }

    public void addCppmodel_cppdirectory(Cppmodel_cppdirectory cppmodel_cppdirectory) {
        this.cppmodel_cppdirectorys.add(cppmodel_cppdirectory);
    }
    public cppmodel_CPPPackage getCppmodel_cpppackage() {
        return cppmodel_cpppackage;
    }

    public void setCppmodel_cpppackage(cppmodel_CPPPackage cppmodel_cpppackage) {
        this.cppmodel_cpppackage = cppmodel_cpppackage;
    }
    public cppmodel_CPPModel getCppmodel_cppmodel() {
        return cppmodel_cppmodel;
    }

    public void setCppmodel_cppmodel(cppmodel_CPPModel cppmodel_cppmodel) {
        this.cppmodel_cppmodel = cppmodel_cppmodel;
    }
    public cppmodel_CPPModel getCppmodel_cppmodel() {
        return cppmodel_cppmodel;
    }

    public void setCppmodel_cppmodel(cppmodel_CPPModel cppmodel_cppmodel) {
        this.cppmodel_cppmodel = cppmodel_cppmodel;
    }
    public cppmodel_CPPPackage getCppmodel_cpppackage() {
        return cppmodel_cpppackage;
    }

    public void setCppmodel_cpppackage(cppmodel_CPPPackage cppmodel_cpppackage) {
        this.cppmodel_cpppackage = cppmodel_cpppackage;
    }
    public cppmodel_CPPComponent getCppmodel_cppcomponent() {
        return cppmodel_cppcomponent;
    }

    public void setCppmodel_cppcomponent(cppmodel_CPPComponent cppmodel_cppcomponent) {
        this.cppmodel_cppcomponent = cppmodel_cppcomponent;
    }
    public cppmodel_CPPComponent getCppmodel_cppcomponent() {
        return cppmodel_cppcomponent;
    }

    public void setCppmodel_cppcomponent(cppmodel_CPPComponent cppmodel_cppcomponent) {
        this.cppmodel_cppcomponent = cppmodel_cppcomponent;
    }
    public cppmodel_CPPComponent getCppmodel_cppcomponent() {
        return cppmodel_cppcomponent;
    }

    public void setCppmodel_cppcomponent(cppmodel_CPPComponent cppmodel_cppcomponent) {
        this.cppmodel_cppcomponent = cppmodel_cppcomponent;
    }
    public cppmodel_CPPModel getCppmodel_cppmodel() {
        return cppmodel_cppmodel;
    }

    public void setCppmodel_cppmodel(cppmodel_CPPModel cppmodel_cppmodel) {
        this.cppmodel_cppmodel = cppmodel_cppmodel;
    }
    public cppmodel_CPPModel getCppmodel_cppmodel() {
        return cppmodel_cppmodel;
    }

    public void setCppmodel_cppmodel(cppmodel_CPPModel cppmodel_cppmodel) {
        this.cppmodel_cppmodel = cppmodel_cppmodel;
    }

}