




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class lobj_AccessControl  {

    private LocalDate lastStatusChange;
    private boolean globalAccess;
    private String status;
    private String id;
    private LocalDate lastModified;





    private lobj_Block lobj_block;




    private lobj_ResrcFile lobj_resrcfile;




    private lobj_BlockFolder lobj_blockfolder;




    private lobj_LearningUnit lobj_learningunit;




    private lobj_Module lobj_module;




    private lobj_ResrcFolder lobj_resrcfolder;




    private lobj_LuFolder lobj_lufolder;




    private lobj_ModuleFolder lobj_modulefolder;


    public lobj_AccessControl(
        LocalDate lastStatusChange,        boolean globalAccess,        String status,        String id,        LocalDate lastModified    ) {
        this.lastStatusChange = lastStatusChange;
        this.globalAccess = globalAccess;
        this.status = status;
        this.id = id;
        this.lastModified = lastModified;
    }


    public LocalDate getLaststatuschange() {
        return lastStatusChange;
    }

    public void setLaststatuschange(LocalDate lastStatusChange) {
        this.lastStatusChange = lastStatusChange;
    }
    public boolean getGlobalaccess() {
        return globalAccess;
    }

    public void setGlobalaccess(boolean globalAccess) {
        this.globalAccess = globalAccess;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public LocalDate getLastmodified() {
        return lastModified;
    }

    public void setLastmodified(LocalDate lastModified) {
        this.lastModified = lastModified;
    }

    public lobj_Block getLobj_block() {
        return lobj_block;
    }

    public void setLobj_block(lobj_Block lobj_block) {
        this.lobj_block = lobj_block;
    }
    public lobj_ResrcFile getLobj_resrcfile() {
        return lobj_resrcfile;
    }

    public void setLobj_resrcfile(lobj_ResrcFile lobj_resrcfile) {
        this.lobj_resrcfile = lobj_resrcfile;
    }
    public lobj_BlockFolder getLobj_blockfolder() {
        return lobj_blockfolder;
    }

    public void setLobj_blockfolder(lobj_BlockFolder lobj_blockfolder) {
        this.lobj_blockfolder = lobj_blockfolder;
    }
    public lobj_LearningUnit getLobj_learningunit() {
        return lobj_learningunit;
    }

    public void setLobj_learningunit(lobj_LearningUnit lobj_learningunit) {
        this.lobj_learningunit = lobj_learningunit;
    }
    public lobj_Module getLobj_module() {
        return lobj_module;
    }

    public void setLobj_module(lobj_Module lobj_module) {
        this.lobj_module = lobj_module;
    }
    public lobj_ResrcFolder getLobj_resrcfolder() {
        return lobj_resrcfolder;
    }

    public void setLobj_resrcfolder(lobj_ResrcFolder lobj_resrcfolder) {
        this.lobj_resrcfolder = lobj_resrcfolder;
    }
    public lobj_LuFolder getLobj_lufolder() {
        return lobj_lufolder;
    }

    public void setLobj_lufolder(lobj_LuFolder lobj_lufolder) {
        this.lobj_lufolder = lobj_lufolder;
    }
    public lobj_ModuleFolder getLobj_modulefolder() {
        return lobj_modulefolder;
    }

    public void setLobj_modulefolder(lobj_ModuleFolder lobj_modulefolder) {
        this.lobj_modulefolder = lobj_modulefolder;
    }

}