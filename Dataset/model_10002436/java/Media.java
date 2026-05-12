





import java.util.List;
import java.util.ArrayList;

public class Media  {

    private String mimetype;
    private None mediaPool;
    private String description;
    private int filesize;
    private boolean active;
    private String name;
    private String link;





    private MediaPool mediapool;




    private MediaPool mediapool;


    public Media(
        String mimetype,        None mediaPool,        String description,        int filesize,        boolean active,        String name,        String link    ) {
        this.mimetype = mimetype;
        this.mediaPool = mediaPool;
        this.description = description;
        this.filesize = filesize;
        this.active = active;
        this.name = name;
        this.link = link;
    }


    public String getMimetype() {
        return mimetype;
    }

    public void setMimetype(String mimetype) {
        this.mimetype = mimetype;
    }
    public None getMediapool() {
        return mediaPool;
    }

    public void setMediapool(None mediaPool) {
        this.mediaPool = mediaPool;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public int getFilesize() {
        return filesize;
    }

    public void setFilesize(int filesize) {
        this.filesize = filesize;
    }
    public boolean getActive() {
        return active;
    }

    public void setActive(boolean active) {
        this.active = active;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getLink() {
        return link;
    }

    public void setLink(String link) {
        this.link = link;
    }

    public MediaPool getMediapool() {
        return mediapool;
    }

    public void setMediapool(MediaPool mediapool) {
        this.mediapool = mediapool;
    }
    public MediaPool getMediapool() {
        return mediapool;
    }

    public void setMediapool(MediaPool mediapool) {
        this.mediapool = mediapool;
    }

}