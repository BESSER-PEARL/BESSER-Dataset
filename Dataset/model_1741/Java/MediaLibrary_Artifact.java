





import java.util.List;
import java.util.ArrayList;

public class MediaLibrary_Artifact  {

    private String name;
    private String author;





    private MediaLibrary_MediaSource medialibrary_mediasource;




    private MediaLibrary_MediaSource medialibrary_mediasource;




    private MediaLibrary_Ecosystem medialibrary_ecosystem;


    public MediaLibrary_Artifact(
        String name,        String author    ) {
        this.name = name;
        this.author = author;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }

    public MediaLibrary_MediaSource getMedialibrary_mediasource() {
        return medialibrary_mediasource;
    }

    public void setMedialibrary_mediasource(MediaLibrary_MediaSource medialibrary_mediasource) {
        this.medialibrary_mediasource = medialibrary_mediasource;
    }
    public MediaLibrary_MediaSource getMedialibrary_mediasource() {
        return medialibrary_mediasource;
    }

    public void setMedialibrary_mediasource(MediaLibrary_MediaSource medialibrary_mediasource) {
        this.medialibrary_mediasource = medialibrary_mediasource;
    }
    public MediaLibrary_Ecosystem getMedialibrary_ecosystem() {
        return medialibrary_ecosystem;
    }

    public void setMedialibrary_ecosystem(MediaLibrary_Ecosystem medialibrary_ecosystem) {
        this.medialibrary_ecosystem = medialibrary_ecosystem;
    }

}