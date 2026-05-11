





import java.util.List;
import java.util.ArrayList;

public class HibernateTest_Bz380987_Person  {

    private String name;





    private List<HibernateTest_Bz380987_Group> hibernatetest_bz380987_groups;




    private HibernateTest_Bz380987_Group hibernatetest_bz380987_group;


    public HibernateTest_Bz380987_Person(
        String name    ) {
        this.name = name;
        this.hibernatetest_bz380987_groups = new ArrayList<>();
    }

    public HibernateTest_Bz380987_Person(
        String name        ArrayList<HibernateTest_Bz380987_Group> hibernatetest_bz380987_groups    ) {
        this.name = name;
        this.hibernatetest_bz380987_groups = hibernatetest_bz380987_groups;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<HibernateTest_Bz380987_Group> getHibernatetest_bz380987_groups() {
        return hibernatetest_bz380987_groups;
    }

    public void addHibernatetest_bz380987_group(Hibernatetest_bz380987_group hibernatetest_bz380987_group) {
        this.hibernatetest_bz380987_groups.add(hibernatetest_bz380987_group);
    }
    public HibernateTest_Bz380987_Group getHibernatetest_bz380987_group() {
        return hibernatetest_bz380987_group;
    }

    public void setHibernatetest_bz380987_group(HibernateTest_Bz380987_Group hibernatetest_bz380987_group) {
        this.hibernatetest_bz380987_group = hibernatetest_bz380987_group;
    }

}