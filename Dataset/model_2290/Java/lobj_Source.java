





import java.util.List;
import java.util.ArrayList;

public class lobj_Source  {

    private String publishedBy;
    private String subtitle;
    private String pp;
    private String id;
    private String publishDate;
    private String publishedIn;
    private String title;





    private lobj_AbstractContent lobj_abstractcontent;




    private lobj_ResrcFile lobj_resrcfile;


    public lobj_Source(
        String publishedBy,        String subtitle,        String pp,        String id,        String publishDate,        String publishedIn,        String title    ) {
        this.publishedBy = publishedBy;
        this.subtitle = subtitle;
        this.pp = pp;
        this.id = id;
        this.publishDate = publishDate;
        this.publishedIn = publishedIn;
        this.title = title;
    }


    public String getPublishedby() {
        return publishedBy;
    }

    public void setPublishedby(String publishedBy) {
        this.publishedBy = publishedBy;
    }
    public String getSubtitle() {
        return subtitle;
    }

    public void setSubtitle(String subtitle) {
        this.subtitle = subtitle;
    }
    public String getPp() {
        return pp;
    }

    public void setPp(String pp) {
        this.pp = pp;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getPublishdate() {
        return publishDate;
    }

    public void setPublishdate(String publishDate) {
        this.publishDate = publishDate;
    }
    public String getPublishedin() {
        return publishedIn;
    }

    public void setPublishedin(String publishedIn) {
        this.publishedIn = publishedIn;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public lobj_AbstractContent getLobj_abstractcontent() {
        return lobj_abstractcontent;
    }

    public void setLobj_abstractcontent(lobj_AbstractContent lobj_abstractcontent) {
        this.lobj_abstractcontent = lobj_abstractcontent;
    }
    public lobj_ResrcFile getLobj_resrcfile() {
        return lobj_resrcfile;
    }

    public void setLobj_resrcfile(lobj_ResrcFile lobj_resrcfile) {
        this.lobj_resrcfile = lobj_resrcfile;
    }

}