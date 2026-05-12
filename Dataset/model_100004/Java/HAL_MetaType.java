





import java.util.List;
import java.util.ArrayList;

public class HAL_MetaType  {

    private String datevisible;
    private String idext;
    private String isEpl;
    private String classification;
    private String collaboration;
    private String keyword;
    private String title;
    private String langue;
    private String refInterne;
    private String researchteam;
    private String comment;
    private String financement;
    private String isEpj;



    public HAL_MetaType(
        String datevisible,        String idext,        String isEpl,        String classification,        String collaboration,        String keyword,        String title,        String langue,        String refInterne,        String researchteam,        String comment,        String financement,        String isEpj    ) {
        this.datevisible = datevisible;
        this.idext = idext;
        this.isEpl = isEpl;
        this.classification = classification;
        this.collaboration = collaboration;
        this.keyword = keyword;
        this.title = title;
        this.langue = langue;
        this.refInterne = refInterne;
        this.researchteam = researchteam;
        this.comment = comment;
        this.financement = financement;
        this.isEpj = isEpj;
    }


    public String getDatevisible() {
        return datevisible;
    }

    public void setDatevisible(String datevisible) {
        this.datevisible = datevisible;
    }
    public String getIdext() {
        return idext;
    }

    public void setIdext(String idext) {
        this.idext = idext;
    }
    public String getIsepl() {
        return isEpl;
    }

    public void setIsepl(String isEpl) {
        this.isEpl = isEpl;
    }
    public String getClassification() {
        return classification;
    }

    public void setClassification(String classification) {
        this.classification = classification;
    }
    public String getCollaboration() {
        return collaboration;
    }

    public void setCollaboration(String collaboration) {
        this.collaboration = collaboration;
    }
    public String getKeyword() {
        return keyword;
    }

    public void setKeyword(String keyword) {
        this.keyword = keyword;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getLangue() {
        return langue;
    }

    public void setLangue(String langue) {
        this.langue = langue;
    }
    public String getRefinterne() {
        return refInterne;
    }

    public void setRefinterne(String refInterne) {
        this.refInterne = refInterne;
    }
    public String getResearchteam() {
        return researchteam;
    }

    public void setResearchteam(String researchteam) {
        this.researchteam = researchteam;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getFinancement() {
        return financement;
    }

    public void setFinancement(String financement) {
        this.financement = financement;
    }
    public String getIsepj() {
        return isEpj;
    }

    public void setIsepj(String isEpj) {
        this.isEpj = isEpj;
    }


}