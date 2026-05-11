





import java.util.List;
import java.util.ArrayList;

public class afpText_DataObjectFontDescriptor extends triplet {

    private String DOFtFlgs;
    private String VFS;
    private String EncID;
    private String EncEnv;
    private String Reserved;
    private String FontTech;
    private String HFS;
    private String CharRot;



    public afpText_DataObjectFontDescriptor(
        String DOFtFlgs,        String VFS,        String EncID,        String EncEnv,        String Reserved,        String FontTech,        String HFS,        String CharRot    ) {
        super(
        );
        this.DOFtFlgs = DOFtFlgs;
        this.VFS = VFS;
        this.EncID = EncID;
        this.EncEnv = EncEnv;
        this.Reserved = Reserved;
        this.FontTech = FontTech;
        this.HFS = HFS;
        this.CharRot = CharRot;
    }


    public String getDoftflgs() {
        return DOFtFlgs;
    }

    public void setDoftflgs(String DOFtFlgs) {
        this.DOFtFlgs = DOFtFlgs;
    }
    public String getVfs() {
        return VFS;
    }

    public void setVfs(String VFS) {
        this.VFS = VFS;
    }
    public String getEncid() {
        return EncID;
    }

    public void setEncid(String EncID) {
        this.EncID = EncID;
    }
    public String getEncenv() {
        return EncEnv;
    }

    public void setEncenv(String EncEnv) {
        this.EncEnv = EncEnv;
    }
    public String getReserved() {
        return Reserved;
    }

    public void setReserved(String Reserved) {
        this.Reserved = Reserved;
    }
    public String getFonttech() {
        return FontTech;
    }

    public void setFonttech(String FontTech) {
        this.FontTech = FontTech;
    }
    public String getHfs() {
        return HFS;
    }

    public void setHfs(String HFS) {
        this.HFS = HFS;
    }
    public String getCharrot() {
        return CharRot;
    }

    public void setCharrot(String CharRot) {
        this.CharRot = CharRot;
    }


}