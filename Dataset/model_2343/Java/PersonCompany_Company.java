





import java.util.List;
import java.util.ArrayList;

public class PersonCompany_Company  {

    private String name;





    private PersonCompany_Job personcompany_job;




    private List<PersonCompany_Job> personcompany_jobs;


    public PersonCompany_Company(
        String name    ) {
        this.name = name;
        this.personcompany_jobs = new ArrayList<>();
    }

    public PersonCompany_Company(
        String name        ArrayList<PersonCompany_Job> personcompany_jobs    ) {
        this.name = name;
        this.personcompany_jobs = personcompany_jobs;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public PersonCompany_Job getPersoncompany_job() {
        return personcompany_job;
    }

    public void setPersoncompany_job(PersonCompany_Job personcompany_job) {
        this.personcompany_job = personcompany_job;
    }
    public List<PersonCompany_Job> getPersoncompany_jobs() {
        return personcompany_jobs;
    }

    public void addPersoncompany_job(Personcompany_job personcompany_job) {
        this.personcompany_jobs.add(personcompany_job);
    }

}