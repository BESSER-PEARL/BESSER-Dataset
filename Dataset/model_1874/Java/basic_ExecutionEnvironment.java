





import java.util.List;
import java.util.ArrayList;

public class basic_ExecutionEnvironment  {

    private String coreType;
    private String name;
    private String corePath;
    private boolean builtin;
    private String facet;
    private String libraries;
    private String versions;



    public basic_ExecutionEnvironment(
        String coreType,        String name,        String corePath,        boolean builtin,        String facet,        String libraries,        String versions    ) {
        this.coreType = coreType;
        this.name = name;
        this.corePath = corePath;
        this.builtin = builtin;
        this.facet = facet;
        this.libraries = libraries;
        this.versions = versions;
    }


    public String getCoretype() {
        return coreType;
    }

    public void setCoretype(String coreType) {
        this.coreType = coreType;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getCorepath() {
        return corePath;
    }

    public void setCorepath(String corePath) {
        this.corePath = corePath;
    }
    public boolean getBuiltin() {
        return builtin;
    }

    public void setBuiltin(boolean builtin) {
        this.builtin = builtin;
    }
    public String getFacet() {
        return facet;
    }

    public void setFacet(String facet) {
        this.facet = facet;
    }
    public String getLibraries() {
        return libraries;
    }

    public void setLibraries(String libraries) {
        this.libraries = libraries;
    }
    public String getVersions() {
        return versions;
    }

    public void setVersions(String versions) {
        this.versions = versions;
    }


}