




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class effbdpattern_SystemPattern extends Indexable {

    private String alias;
    private String description;
    private String name;
    private String challeng;
    private LocalDate creationDate;
    private String knownApplications;
    private int patternId;





    private effbdpattern_ModelElement effbdpattern_modelelement;




    private List<effbdpattern_SystemPattern> effbdpattern_systempatterns;




    private effbdpattern_ModelElement effbdpattern_modelelement;




    private effbdpattern_Problem effbdpattern_problem;




    private List<effbdpattern_SystemPattern> effbdpattern_systempatterns;




    private effbdpattern_SystemPattern effbdpattern_systempattern;




    private List<effbdpattern_SystemPattern> effbdpattern_systempatterns;




    private effbdpattern_Domain effbdpattern_domain;




    private effbdpattern_Context effbdpattern_context;


    public effbdpattern_SystemPattern(
        String alias,        String description,        String name,        String challeng,        LocalDate creationDate,        String knownApplications,        int patternId    ) {
        super(
        );
        this.alias = alias;
        this.description = description;
        this.name = name;
        this.challeng = challeng;
        this.creationDate = creationDate;
        this.knownApplications = knownApplications;
        this.patternId = patternId;
        this.effbdpattern_systempatterns = new ArrayList<>();
        this.effbdpattern_systempatterns = new ArrayList<>();
        this.effbdpattern_systempatterns = new ArrayList<>();
    }

    public effbdpattern_SystemPattern(
        String alias,        String description,        String name,        String challeng,        LocalDate creationDate,        String knownApplications,        int patternId        ArrayList<effbdpattern_SystemPattern> effbdpattern_systempatterns,        ArrayList<effbdpattern_SystemPattern> effbdpattern_systempatterns,        ArrayList<effbdpattern_SystemPattern> effbdpattern_systempatterns    ) {
        this.alias = alias;
        this.description = description;
        this.name = name;
        this.challeng = challeng;
        this.creationDate = creationDate;
        this.knownApplications = knownApplications;
        this.patternId = patternId;
        this.effbdpattern_systempatterns = effbdpattern_systempatterns;
        this.effbdpattern_systempatterns = effbdpattern_systempatterns;
        this.effbdpattern_systempatterns = effbdpattern_systempatterns;
    }

    public String getAlias() {
        return alias;
    }

    public void setAlias(String alias) {
        this.alias = alias;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getChalleng() {
        return challeng;
    }

    public void setChalleng(String challeng) {
        this.challeng = challeng;
    }
    public LocalDate getCreationdate() {
        return creationDate;
    }

    public void setCreationdate(LocalDate creationDate) {
        this.creationDate = creationDate;
    }
    public String getKnownapplications() {
        return knownApplications;
    }

    public void setKnownapplications(String knownApplications) {
        this.knownApplications = knownApplications;
    }
    public int getPatternid() {
        return patternId;
    }

    public void setPatternid(int patternId) {
        this.patternId = patternId;
    }

    public effbdpattern_ModelElement getEffbdpattern_modelelement() {
        return effbdpattern_modelelement;
    }

    public void setEffbdpattern_modelelement(effbdpattern_ModelElement effbdpattern_modelelement) {
        this.effbdpattern_modelelement = effbdpattern_modelelement;
    }
    public List<effbdpattern_SystemPattern> getEffbdpattern_systempatterns() {
        return effbdpattern_systempatterns;
    }

    public void addEffbdpattern_systempattern(Effbdpattern_systempattern effbdpattern_systempattern) {
        this.effbdpattern_systempatterns.add(effbdpattern_systempattern);
    }
    public effbdpattern_ModelElement getEffbdpattern_modelelement() {
        return effbdpattern_modelelement;
    }

    public void setEffbdpattern_modelelement(effbdpattern_ModelElement effbdpattern_modelelement) {
        this.effbdpattern_modelelement = effbdpattern_modelelement;
    }
    public effbdpattern_Problem getEffbdpattern_problem() {
        return effbdpattern_problem;
    }

    public void setEffbdpattern_problem(effbdpattern_Problem effbdpattern_problem) {
        this.effbdpattern_problem = effbdpattern_problem;
    }
    public List<effbdpattern_SystemPattern> getEffbdpattern_systempatterns() {
        return effbdpattern_systempatterns;
    }

    public void addEffbdpattern_systempattern(Effbdpattern_systempattern effbdpattern_systempattern) {
        this.effbdpattern_systempatterns.add(effbdpattern_systempattern);
    }
    public effbdpattern_SystemPattern getEffbdpattern_systempattern() {
        return effbdpattern_systempattern;
    }

    public void setEffbdpattern_systempattern(effbdpattern_SystemPattern effbdpattern_systempattern) {
        this.effbdpattern_systempattern = effbdpattern_systempattern;
    }
    public List<effbdpattern_SystemPattern> getEffbdpattern_systempatterns() {
        return effbdpattern_systempatterns;
    }

    public void addEffbdpattern_systempattern(Effbdpattern_systempattern effbdpattern_systempattern) {
        this.effbdpattern_systempatterns.add(effbdpattern_systempattern);
    }
    public effbdpattern_Domain getEffbdpattern_domain() {
        return effbdpattern_domain;
    }

    public void setEffbdpattern_domain(effbdpattern_Domain effbdpattern_domain) {
        this.effbdpattern_domain = effbdpattern_domain;
    }
    public effbdpattern_Context getEffbdpattern_context() {
        return effbdpattern_context;
    }

    public void setEffbdpattern_context(effbdpattern_Context effbdpattern_context) {
        this.effbdpattern_context = effbdpattern_context;
    }

}