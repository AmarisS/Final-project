# Title: Monte Carlo Simulation on Airport Security Check

## Team Member(s): Sixuan Shen, Mengfei Liang

## Monte Carlo Simulation Scenario & Purpose:
Scenario：In our project, we simulate the airport security check. According to the real life situation, the wait time in the security check is decided by various variables. As we all know, the volume of passengers obviously increase on big holidays, like the Thanksgiving break or Christmas. Meanwhile, even on the normal week, the wait time of the security check may differ between weekdays and weekends. This project plan to simulate the security check on weekdays (not in holidays) scenario, on weekends(not in holidays) scenario, on holiday scenario. This subdivision scenario could better simulate the real-life airport security check.

Purpose：With the rapid development of transportation, more and more people tend to choose airplane as their travel tool. But before getting on the plane, the passengers are supposed to pass the airport check and the time of airport check is unsure. This Monte Carlo simulation on airport security check simulates scenarios in different time period, which can provide passengers a estimated wait time in the checkpoint. Not only on the normal days, but also on special holidays, people are able to know when they need to arrive at the security checkpoint in advance so that they can catch on their plane in time.

The data this project used to simulate the real-life situation is from Whatsbusy website. And we choose Chicago Ohare Airport to simulate by setting the terminal(international or domestic) variable, date variable, etc.

## Hypothesis before running the simulation:

* security check entrance in the airport: 5

Assumptions:
* Each passengers passing the security check is independent and identity distributed.
* The security check counter treat passengers at same speed. (* If time permits, we would add a additional exception 
  situation: if people is regarded as carrying prohibited items, the check counter which deal with this situation will    
  temporarily close.)
* The security checkpoint can treat 180 passengers at an hour.

Hypothesis:

* On weekdays in normal week, passenger’s average passing time for security check is 0-10min.
* On Firday, passenger’s average passing time will increase by 5-10min than in normal week.
* During holidays, passenger’s average passing time would double when compared with time on same day in normal week.

## Simulation's variables of uncertainty
* date_time:The number of passengers come to the airport during a certain date and time. The date is used to determine whether 
  today is in weekday or in weekend. And whether it is around the holiday(from two days before the holiday and two days after   the holiday). There are four time ranges in one day, 6am-12pm, 12pm-6pm,6pm-12am,12am-6am.
* secheck_time: The security check time for each passenger. This variable is also random for each passenger, the number would   be between 1s to 120s. 
* extra_checktime: Additional security check time for those passengers bring liquid, and other things that cannot be taken on   board. The system would pick up those passengers need extra security check time randomly, the probability would between   
  1/500 and 1/10.

## Instructions on how to use the program:
After running this program, users would need to input their date and time period of when they would arrive the airport. And the output of the program is the average wait time for passengers in the security checkpoint in this period.
With the output from the simulation, it's able to compare it with the former hypothesis. Is the average wait time of security check would be between 10 and 15 minutes? Is the average wait time during the weekend would be greater than the average wait time during the weekdays? 
Our program aims to be a useful tuturiol for passengers, they can easily check how long they should arrive in advance to pass the airport security check in time.

## Conclusions:
We have tested average waiting time on weekdays, on Friday, and during Christmas holiday(from Dec.23 to Dec.27), and usually the time range would fall between 300s to 800s, which is between 5 minutes to 12 minutes. On holiday, the time range with usually fall between 600s and 1800s, which is between 10 minutes and 30 minutes. The results quite approves the hypothesis.

## How to run the program:
After running this program, please input the date and time in the form of 06.00 10.00 Dec.15 2018 or 06.00 10.00 Dec.15, and enter. If you do not input the year, then the system would use the default year:2017. 20 results of estimated waiting time, the minimum and maximum values of those 20 results, and a scatter plot would be shown on the screen. Then you would need to click the close button of that plot and input "y/n" to decide whether to continue entering date and time of arriving the airport. 
## Sources Used:
* Reference Data：http://www.whatsbusy.com/airport/MCO/20171129T020000 
* Monte Carlo Simulation：https://en.wikipedia.org/wiki/Monte_Carlo_method                               https://courses.ischool.illinois.edu/pluginfile.php/335371/mod_resource/content/1/MillerRanum%203.4%20Queues%20%20Simulations.pdf
