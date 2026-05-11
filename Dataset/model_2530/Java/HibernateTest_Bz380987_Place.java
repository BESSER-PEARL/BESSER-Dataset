





import java.util.List;
import java.util.ArrayList;

public class HibernateTest_Bz380987_Place  {

    private String name;





    private List<HibernateTest_Bz380987_Person> hibernatetest_bz380987_persons;




    private HibernateTest_Bz380987_Person hibernatetest_bz380987_person;


    public HibernateTest_Bz380987_Place(
        String name    ) {
        this.name = name;
        this.hibernatetest_bz380987_persons = new ArrayList<>();
    }

    public HibernateTest_Bz380987_Place(
        String name        ArrayList<HibernateTest_Bz380987_Person> hibernatetest_bz380987_persons    ) {
        this.name = name;
        this.hibernatetest_bz380987_persons = hibernatetest_bz380987_persons;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<HibernateTest_Bz380987_Person> getHibernatetest_bz380987_persons() {
        return hibernatetest_bz380987_persons;
    }

    public void addHibernatetest_bz380987_person(Hibernatetest_bz380987_person hibernatetest_bz380987_person) {
        this.hibernatetest_bz380987_persons.add(hibernatetest_bz380987_person);
    }
    public HibernateTest_Bz380987_Person getHibernatetest_bz380987_person() {
        return hibernatetest_bz380987_person;
    }

    public void setHibernatetest_bz380987_person(HibernateTest_Bz380987_Person hibernatetest_bz380987_person) {
        this.hibernatetest_bz380987_person = hibernatetest_bz380987_person;
    }

}