





import java.util.List;
import java.util.ArrayList;

public class builds_ChangeArtifact  {

    private String editType;
    private String relativePath;
    private String prevRevision;
    private String file;
    private boolean dead;
    private String revision;





    private builds_Change builds_change;


    public builds_ChangeArtifact(
        String editType,        String relativePath,        String prevRevision,        String file,        boolean dead,        String revision    ) {
        this.editType = editType;
        this.relativePath = relativePath;
        this.prevRevision = prevRevision;
        this.file = file;
        this.dead = dead;
        this.revision = revision;
    }


    public String getEdittype() {
        return editType;
    }

    public void setEdittype(String editType) {
        this.editType = editType;
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
    public String getFile() {
        return file;
    }

    public void setFile(String file) {
        this.file = file;
    }
    public boolean getDead() {
        return dead;
    }

    public void setDead(boolean dead) {
        this.dead = dead;
    }
    public String getRevision() {
        return revision;
    }

    public void setRevision(String revision) {
        this.revision = revision;
    }

    public builds_Change getBuilds_change() {
        return builds_change;
    }

    public void setBuilds_change(builds_Change builds_change) {
        this.builds_change = builds_change;
    }

}