





import java.util.List;
import java.util.ArrayList;

public class Editoriales  {

    private String direcci_nEmail;
    private String n_meroTel_fono;
    private String personaContacto;
    private String direcci_nF_sica;





    private List<Documentos> documentoss;


    public Editoriales(
        String direcci_nEmail,        String n_meroTel_fono,        String personaContacto,        String direcci_nF_sica    ) {
        this.direcci_nEmail = direcci_nEmail;
        this.n_meroTel_fono = n_meroTel_fono;
        this.personaContacto = personaContacto;
        this.direcci_nF_sica = direcci_nF_sica;
        this.documentoss = new ArrayList<>();
    }

    public Editoriales(
        String direcci_nEmail,        String n_meroTel_fono,        String personaContacto,        String direcci_nF_sica        ArrayList<Documentos> documentoss    ) {
        this.direcci_nEmail = direcci_nEmail;
        this.n_meroTel_fono = n_meroTel_fono;
        this.personaContacto = personaContacto;
        this.direcci_nF_sica = direcci_nF_sica;
        this.documentoss = documentoss;
    }

    public String getDirecci_nemail() {
        return direcci_nEmail;
    }

    public void setDirecci_nemail(String direcci_nEmail) {
        this.direcci_nEmail = direcci_nEmail;
    }
    public String getN_merotel_fono() {
        return n_meroTel_fono;
    }

    public void setN_merotel_fono(String n_meroTel_fono) {
        this.n_meroTel_fono = n_meroTel_fono;
    }
    public String getPersonacontacto() {
        return personaContacto;
    }

    public void setPersonacontacto(String personaContacto) {
        this.personaContacto = personaContacto;
    }
    public String getDirecci_nf_sica() {
        return direcci_nF_sica;
    }

    public void setDirecci_nf_sica(String direcci_nF_sica) {
        this.direcci_nF_sica = direcci_nF_sica;
    }

    public List<Documentos> getDocumentoss() {
        return documentoss;
    }

    public void addDocumentos(Documentos documentos) {
        this.documentoss.add(documentos);
    }

}