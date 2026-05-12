





import java.util.List;
import java.util.ArrayList;

public class Beitrag  {

    private String foto;
    private String Audio;
    private String video;
    private String privatph_re;
    private String text;





    private Benutzer benutzer;


    public Beitrag(
        String foto,        String Audio,        String video,        String privatph_re,        String text    ) {
        this.foto = foto;
        this.Audio = Audio;
        this.video = video;
        this.privatph_re = privatph_re;
        this.text = text;
    }


    public String getFoto() {
        return foto;
    }

    public void setFoto(String foto) {
        this.foto = foto;
    }
    public String getAudio() {
        return Audio;
    }

    public void setAudio(String Audio) {
        this.Audio = Audio;
    }
    public String getVideo() {
        return video;
    }

    public void setVideo(String video) {
        this.video = video;
    }
    public String getPrivatph_re() {
        return privatph_re;
    }

    public void setPrivatph_re(String privatph_re) {
        this.privatph_re = privatph_re;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public Benutzer getBenutzer() {
        return benutzer;
    }

    public void setBenutzer(Benutzer benutzer) {
        this.benutzer = benutzer;
    }

}