





import java.util.List;
import java.util.ArrayList;

public class builds_ChangeArtifact  {

    private boolean dead;
    private String file;
    private String revision;
    private String relativePath;
    private String prevRevision;
    private String editType;





    private builds_Change builds_change;


    public builds_ChangeArtifact(
        boolean dead,        String file,        String revision,        String relativePath,        String prevRevision,        String editType    ) {
        this.dead = dead;
        this.file = file;
        this.revision = revision;
        this.relativePath = relativePath;
        this.prevRevision = prevRevision;
        this.editType = editType;
    }


    public boolean getDead() {
        return dead;
    }

    public void setDead(boolean dead) {
        this.dead = dead;
    }
    public String getFile() {
        return file;
    }

    public void setFile(String file) {
        this.file = file;
    }
    public String getRevision() {
        return revision;
    }

    public void setRevision(String revision) {
        this.revision = revision;
    }
    public String getRelativepath() {
        return relativePath;
    }

    public void setRelativepath(String relativePath) {
        this.relativePath = relativePath;
    }
    public String getPrevrevision() {
        return prevRevision;
    }

    public void setPrevrevision(String prevRevision) {
        this.prevRevision = prevRevision;
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