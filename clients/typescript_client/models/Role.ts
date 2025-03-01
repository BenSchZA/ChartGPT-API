/**
 * ChartGPT API
 * The ChartGPT API is a REST API that generates insights from data based on natural language questions.
 *
 * OpenAPI spec version: 0.1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { HttpFile } from '../http/http';

/**
* The role of the message.
*/
export enum Role {
    System = 'system',
    User = 'user',
    Assistant = 'assistant',
    Function = 'function'
}
