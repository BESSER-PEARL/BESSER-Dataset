





import java.util.List;
import java.util.ArrayList;

public class sourcecleaner_ExtensionReference  {

    private String package;
    private String project;
    private String java;
    private String name;





    private sourcecleaner_Java sourcecleaner_java;




    private sourcecleaner_Schema sourcecleaner_schema;




    private sourcecleaner_Schema sourcecleaner_schema;


    public sourcecleaner_ExtensionReference(
        String package,        String project,        String java,        String name    ) {
        this.package = package;
        this.project = project;
        this.java = java;
        this.name = name;
    }


    public String getPackage() {
        return package;
    }

    public void setPackage(String package) {
        this.package = package;
    }
    public String getProject() {
        return project;
    }

    public void setProject(String project) {
        this.project = project;
    }
    public String getJava() {
        return java;
    }

    public void setJava(String java) {
        this.java = java;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public sourcecleaner_Java getSourcecleaner_java() {
        return sourcecleaner_java;
    }

    public void setSourcecleaner_java(sourcecleaner_Java sourcecleaner_java) {
        this.sourcecleaner_java = sourcecleaner_java;
    }
    public sourcecleaner_Schema getSourcecleaner_schema() {
        return sourcecleaner_schema;
    }

    public void setSourcecleaner_schema(sourcecleaner_Schema sourcecleaner_schema) {
        this.sourcecleaner_schema = sourcecleaner_schema;
    }
    public sourcecleaner_Schema getSourcecleaner_schema() {
        return sourcecleaner_schema;
    }

    public void setSourcecleaner_schema(sourcecleaner_Schema sourcecleaner_schema) {
        this.sourcecleaner_schema = sourcecleaner_schema;
    }

}