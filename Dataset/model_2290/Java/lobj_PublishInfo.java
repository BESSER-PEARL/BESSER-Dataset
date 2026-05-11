




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class lobj_PublishInfo  {

    private String edition;
    private String id;
    private String releaseinfo;
    private LocalDate pubdate;
    private String pubsnumber;





    private lobj_ModuleMeta lobj_modulemeta;




    private lobj_LuMeta lobj_lumeta;


    public lobj_PublishInfo(
        String edition,        String id,        String releaseinfo,        LocalDate pubdate,        String pubsnumber    ) {
        this.edition = edition;
        this.id = id;
        this.releaseinfo = releaseinfo;
        this.pubdate = pubdate;
        this.pubsnumber = pubsnumber;
    }


    public String getEdition() {
        return edition;
    }

    public void setEdition(String edition) {
        this.edition = edition;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getReleaseinfo() {
        return releaseinfo;
    }

    public void setReleaseinfo(String releaseinfo) {
        this.releaseinfo = releaseinfo;
    }
    public LocalDate getPubdate() {
        return pubdate;
    }

    public void setPubdate(LocalDate pubdate) {
        this.pubdate = pubdate;
    }
    public String getPubsnumber() {
        return pubsnumber;
    }

    public void setPubsnumber(String pubsnumber) {
        this.pubsnumber = pubsnumber;
    }

    public lobj_ModuleMeta getLobj_modulemeta() {
        return lobj_modulemeta;
    }

    public void setLobj_modulemeta(lobj_ModuleMeta lobj_modulemeta) {
        this.lobj_modulemeta = lobj_modulemeta;
    }
    public lobj_LuMeta getLobj_lumeta() {
        return lobj_lumeta;
    }

    public void setLobj_lumeta(lobj_LuMeta lobj_lumeta) {
        this.lobj_lumeta = lobj_lumeta;
    }

}