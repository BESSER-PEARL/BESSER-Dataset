





import java.util.List;
import java.util.ArrayList;

public class builds_ChangeArtifact  {

    private String prevRevision;
    private String revision;
    private String file;
    private String relativePath;
    private boolean dead;
    private String editType;





    private builds_Change builds_change;


    public builds_ChangeArtifact(
        String prevRevision,        String revision,        String file,        String relativePath,        boolean dead,        String editType    ) {
        this.prevRevision = prevRevision;
        this.revision = revision;
        this.file = file;
        this.relativePath = relativePath;
        this.dead = dead;
        this.editType = editType;
    }


    public String getPrevrevision() {
        return prevRevision;
    }

    public void setPrevrevision(String prevRevision) {
        this.prevRevision = prevRevision;
    }
    public String getRevision() {
        return revision;
    }

    public void setRevision(String revision) {
        this.revision = revision;
    }
    public String getFile() {
        return file;
    }

    public void setFile(String file) {
        this.file = file;
    }
    public String getRelativepath() {
        return relativePath;
    }

    public void setRelativepath(String relativePath) {
        this.relativePath = relativePath;
    }
    public boolean getDead() {
        return dead;
    }

    public void setDead(boolean dead) {
        this.dead = dead;
    }
    public String getEdittype() {
        return editType;
    }

    public void setEdittype(String editType) {
        this.editType = editType;
    }

    public builds_Change getBuilds_change() {
        return builds_change;
    }

    public void setBuilds_change(builds_Change builds_change) {
        this.builds_change = builds_change;
    }

}