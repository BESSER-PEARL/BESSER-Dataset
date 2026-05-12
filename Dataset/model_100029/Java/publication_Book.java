





import java.util.List;
import java.util.ArrayList;

public class publication_Book extends BiblioReference {

    private String iSBN;
    private String volume;
    private String series;
    private String edition;



    public publication_Book(
        String iSBN,        String volume,        String series,        String edition    ) {
        super(
        );
        this.iSBN = iSBN;
        this.volume = volume;
        this.series = series;
        this.edition = edition;
    }


    public String getIsbn() {
        return iSBN;
    }

    public void setIsbn(String iSBN) {
        this.iSBN = iSBN;
    }
    public String getVolume() {
        return volume;
    }

    public void setVolume(String volume) {
        this.volume = volume;
    }
    public String getSeries() {
        return series;
    }

    public void setSeries(String series) {
        this.series = series;
    }
    public String getEdition() {
        return edition;
    }

    public void setEdition(String edition) {
        this.edition = edition;
    }


}