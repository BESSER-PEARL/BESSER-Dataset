





import java.util.List;
import java.util.ArrayList;

public class Beitrag  {

    private String privatph_re;
    private String foto;
    private String video;
    private String text;
    private String Audio;





    private Benutzer benutzer;




    private Ver_ffentlich ver_ffentlich;




    private List<Group> groups;




    private List<Kommentare> kommentares;




    private Privat privat;


    public Beitrag(
        String privatph_re,        String foto,        String video,        String text,        String Audio    ) {
        this.privatph_re = privatph_re;
        this.foto = foto;
        this.video = video;
        this.text = text;
        this.Audio = Audio;
        this.groups = new ArrayList<>();
        this.kommentares = new ArrayList<>();
    }

    public Beitrag(
        String privatph_re,        String foto,        String video,        String text,        String Audio        ArrayList<Group> groups,        ArrayList<Kommentare> kommentares    ) {
        this.privatph_re = privatph_re;
        this.foto = foto;
        this.video = video;
        this.text = text;
        this.Audio = Audio;
        this.groups = groups;
        this.kommentares = kommentares;
    }

    public String getPrivatph_re() {
        return privatph_re;
    }

    public void setPrivatph_re(String privatph_re) {
        this.privatph_re = privatph_re;
    }
    public String getFoto() {
        return foto;
    }

    public void setFoto(String foto) {
        this.foto = foto;
    }
    public String getVideo() {
        return video;
    }

    public void setVideo(String video) {
        this.video = video;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public String getAudio() {
        return Audio;
    }

    public void setAudio(String Audio) {
        this.Audio = Audio;
    }

    public Benutzer getBenutzer() {
        return benutzer;
    }

    public void setBenutzer(Benutzer benutzer) {
        this.benutzer = benutzer;
    }
    public Ver_ffentlich getVer_ffentlich() {
        return ver_ffentlich;
    }

    public void setVer_ffentlich(Ver_ffentlich ver_ffentlich) {
        this.ver_ffentlich = ver_ffentlich;
    }
    public List<Group> getGroups() {
        return groups;
    }

    public void addGroup(Group group) {
        this.groups.add(group);
    }
    public List<Kommentare> getKommentares() {
        return kommentares;
    }

    public void addKommentare(Kommentare kommentare) {
        this.kommentares.add(kommentare);
    }
    public Privat getPrivat() {
        return privat;
    }

    public void setPrivat(Privat privat) {
        this.privat = privat;
    }

}